from django.contrib import admin
from .models import userProfile
# регистрируем модель.

admin.site.register(userProfile)

admin.site.site_header="main"