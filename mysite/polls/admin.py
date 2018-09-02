# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Poll
from models import Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Data Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    # 日期分层导航
    date_hierarchy = 'pub_date'


admin.site.register(Poll, PollAdmin)

