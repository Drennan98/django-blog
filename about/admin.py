from django.contrib import admin
from .models import About
from django_summernote.admin import SumemernoteModelAdmin

# Register your models here.

@admin.register(About)
class AboutAdmin(SumemernoteModelAdmin):

    summernote_fields = ('content',)