from django.contrib import admin

from .models import *


admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Genres)
admin.site.register(Title)
