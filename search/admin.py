
# Register your models here.
from django.contrib import admin

# Register your models here.
from models import SearchKeyword
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage


class SearchKeywordAdmin(admin.TabularInline):
    model = SearchKeyword


class FlatPageAdmin(FlatPageAdmin):
    inlines = [SearchKeywordAdmin]


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
