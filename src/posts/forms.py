from django import forms
from posts.models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            "title",
            "author",
            "content",
            "published",
            "created_on",
        ]

        widgets = {
            'created_on': forms.SelectDateWidget(years=range(1990, 2040))
        }
