from django.contrib import admin
from signup.models import Signup

class SignupAdmin(admin.ModelAdmin):
	class Meta:
		model = Signup

admin.site.register(Signup,SignupAdmin)
