from django.contrib import admin
from .models import Contact, Thread, Post

# Register your models here.
admin.site.register(Contact)
admin.site.register(Thread)
admin.site.register(Post)