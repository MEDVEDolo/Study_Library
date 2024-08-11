from django.contrib import admin
from Core.models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_editable = ('email',)

@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ('id', 'end', 'user')