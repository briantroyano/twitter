from django.contrib import admin
from .models import Tweet
# Register your models here.

# Simple Search Bar to find users by username or email
class TweetAdmin(admin.ModelAdmin):
    list_display = ['__str__','user']
    search_fields = ['content','user__username', 'user__email']
    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetAdmin)