from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = 'Pollster Admin'
admin.site.site_title = 'Pollster Admin Area'
admin.site.site_title = 'Welcome to the Pollster admin area'

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [ ( None, { 'fields': [ 'question_text' ] } ),
                       ( 'Date Information', { 'fields' : [ 'pub_date' ], 'classes': [ 'collapse' ] } ),
                    ]
    inlines = [ ChoiceInline ]

# Register your models here.
#admin.site.register(Question, Choice)
admin.site.register(Question, QuestionAdmin)
