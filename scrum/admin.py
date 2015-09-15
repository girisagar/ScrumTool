from django.contrib import admin
from scrum.models import (
	ProductBacklog,
	ReleaseBacklog,
	UserStory,
	WorkLog,
	Sprint
)

admin.site.register(ProductBacklog)
admin.site.register(ReleaseBacklog)
admin.site.register(UserStory)
admin.site.register(WorkLog)
admin.site.register(Sprint)