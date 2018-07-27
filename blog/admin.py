from django.contrib import admin

# Register blog model so that it is visible in the admin panel.

from.models import Blog

admin.site.register(Blog)
