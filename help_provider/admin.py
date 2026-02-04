from django.contrib import admin
from .models import HelpPost, Profile, Category

# 1. Customizing HelpPost view
class HelpPostAdmin(admin.ModelAdmin):
    # This shows columns in the list view
    list_display = ('title', 'user', 'help_type', 'city', 'created_at')
    # This adds a filter sidebar on the right
    list_filter = ('help_type', 'status', 'category')
    # This adds a search bar at the top
    search_fields = ('title', 'description', 'city')

# 2. Registering the models
admin.site.register(HelpPost, HelpPostAdmin)
admin.site.register(Profile)
admin.site.register(Category)