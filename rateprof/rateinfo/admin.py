from django.contrib import admin

# Register your models here.
from rateinfo.models import *

admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Response)
admin.site.register(GP)
admin.site.register(Teach)
admin.site.register(GroupChat)

