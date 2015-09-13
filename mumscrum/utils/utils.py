def validate_email_unique(value):
    exists = User.objects.filter(email=value)
    if exists:
        raise ValidationError("Email address %s already exits, must be unique" % value)