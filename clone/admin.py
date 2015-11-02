from django.contrib import admin
from clone.models import People,Movie,Studio
# Register your models here.

class peopleAdmin(admin.ModelAdmin):

	class Meta:
		model = People

admin.site.register(People,peopleAdmin)