from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(User_qualifications)
admin.site.register(User_achievements)
admin.site.register(Forums)
admin.site.register(Subforums)
admin.site.register(Threads)
admin.site.register(Posts)
admin.site.register(forum_mods)
admin.site.register(subforum_mods)
admin.site.register(tags)
admin.site.register(tag_to_subforum)
admin.site.register(tag_to_forum)
admin.site.register(subs_users)
admin.site.register(subs_thread)
admin.site.register(subs_subforum)
admin.site.register(subs_forum)
# Register your models here.
