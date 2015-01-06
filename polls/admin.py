from django.contrib import admin
from polls.models import Question,Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):

	list_display = ('question_text','pub_date','was_published_recently')
	inlines = [ChoiceInline]

	# filtering Question change list
	list_filter = ['question_text','pub_date']
	# search field
	search_fields = ['question_text','pub_date']

admin.site.register(Question,QuestionAdmin)
