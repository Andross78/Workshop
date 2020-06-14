from django.contrib import admin

from .models import Process, Category, User, Car


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    ...

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...