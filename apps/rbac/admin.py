from django.contrib import admin
from .models import Role, Permission

admin.site.register([Role, Permission])
