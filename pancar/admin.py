from django.contrib import admin

from .models import Process, Category


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    ...
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...