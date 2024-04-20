from django.contrib import admin

from contactme.models import sayhi
from contactme.models import contact
# Register your models here.
admin.site.register(sayhi)
admin.site.register(contact)