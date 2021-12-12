from django.contrib import admin
# Register your models here.
from posts.models import BlogPost

@admin.register(BlogPost)
class BlogPost(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "author",
        "created_on",
        "last_updated",
        "published",
        )
    list_filter = ("author", "published",)
    list_display_links = ("slug",)
    list_editable = ("title", "published",)
    search_fields = ("title", "slug", "author",)
    autocomplete_fields = ("author",)
    empty_value_display = "unknown"
    list_per_page = 10

