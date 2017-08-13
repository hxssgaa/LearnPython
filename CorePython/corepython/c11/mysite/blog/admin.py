from django.contrib import admin

import models


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


admin.site.register(models.BlogPost, BlogPostAdmin)
