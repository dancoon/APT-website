from django.contrib import admin
from .models import Member, Contact

# Register your models here.
@admin.register(Member)#avail Member to admin panel
class MemberAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'email', 'position', 'is_active']
    list_filter = ['position', 'is_active']
    search_fields = ['fname', 'lname', 'email']
    list_editable = ['lname', 'email', 'is_active', 'position']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname']
    list_filter = ['fname','lname']
    search_fields = ['fname', 'lname']
    
