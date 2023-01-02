from django.contrib import admin
from .models import *
from guardian.admin import GuardedModelAdmin
# Register your models here.

admin.site.register(Player)
admin.site.register(Umpire)
admin.site.register(Umpiredby)
admin.site.register(Matches)
admin.site.register(Teammanagement)
admin.site.register(Captain)
admin.site.register(Plays)
@admin.register(Team)



class TeamAdmin(GuardedModelAdmin):
    list_display = ('teamname',)
