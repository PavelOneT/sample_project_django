from django.contrib import admin
from bboard.models import Bb, Rubric



class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'Rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Rubric)
admin.site.register(Bb, BbAdmin)

