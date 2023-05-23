from django.contrib import admin
from .models import UZVerb, Choice


# Register your models here.
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 0


class ChoiceAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]


admin.site.register(UZVerb, ChoiceAdmin)
