from django.http import HttpResponseRedirect
from django.conf import settings
from django.db import connection
from time import time
from operator import add
import re
from re import compile

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]

if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware:
    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings via a list of regular expressions in LOGIN_EXEMPT_URLS (which
    you can copy from your urls.py).

    Requires authentication middleware and template context processors to be
    loaded. You'll get an error if they aren't.
    """
    def process_request(self, request):
        assert hasattr(request, 'user'), "The Login Required middleware\
 requires authentication middleware to be installed. Edit your\
 MIDDLEWARE_CLASSES setting to insert\
 'django.contrib.auth.middlware.AuthenticationMiddleware'. If that doesn't\
 work, ensure your TEMPLATE_CONTEXT_PROCESSORS setting includes\
 'django.core.context_processors.auth'."
        if not request.user.is_authenticated():
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                return HttpResponseRedirect(settings.LOGIN_URL)


class StatsMiddleware(object):

    def process_view(self, request, view_func, view_args, view_kwargs):
        '''
        In your base template, put this:
        <div id="stats">
        <!-- STATS: Total: %(total_time).2fs Python: %(python_time).2fs DB: %(db_time).2fs Queries: %(db_queries)d ENDSTATS -->
        </div>
        '''

        # Uncomment the following if you want to get stats on DEBUG=True only
        #if not settings.DEBUG:
        #    return None

        # get number of db queries before we do anything
        n = len(connection.queries)

        # time the view
        start = time()
        response = view_func(request, *view_args, **view_kwargs)
        total_time = time() - start

        # compute the db time for the queries just run
        db_queries = len(connection.queries) - n
        if db_queries:
            db_time = reduce(add, [float(q['time'])
                                   for q in connection.queries[n:]])
        else:
            db_time = 0.0

        # and backout python time
        python_time = total_time - db_time

        stats = {
            'total_time': total_time,
            'python_time': python_time,
            'db_time': db_time,
            'db_queries': db_queries,
        }

        # replace the comment if found
        if response:
            try:
                # detects TemplateResponse which are not yet rendered
                if response.is_rendered:
                    rendered_content = response.content
                else:
                    rendered_content = response.rendered_content
            except AttributeError:  # django < 1.5
                # rendered_content = response.content
                pass
            else:
                if rendered_content:
                    s = rendered_content
                    regexp = re.compile(
                        r'(?P<cmt><!--\s*STATS:(?P<fmt>.*?)ENDSTATS\s*-->)'
                    )
                    match = regexp.search(s)
                    if match:
                        s = (s[:match.start('cmt')] +
                             match.group('fmt') % stats +
                             s[match.end('cmt'):])
                        response.content = s
        return response