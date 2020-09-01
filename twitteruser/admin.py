from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    #got help from stackoverflow
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field to show on admin (extra credit)',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'display_name',             
                  
                ),
            },
        ),
    )
admin.site.register(models.TwitterUserModel,CustomUserAdmin)