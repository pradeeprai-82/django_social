from django.contrib import admin
from blog.models import Blogpost
from blog.models import Blogcomment
from blog.models import Contact

# Register your models here.
admin.site.register(Blogpost)
admin.site.register(Blogcomment)
admin.site.register(Contact)
