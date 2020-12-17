from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import Group
from django.contrib.auth import get_user_model
from .forms import CustomChangeForm, CustomCreationForm
User = get_user_model()

@admin.register(User)
class UserAdmin(BaseUserAdmin):

  # form = CustomChangeForm
  # add_form = CustomCreationForm

  list_display = ('email', 'nickname',)
  list_filter = ('is_admin' ,'is_active',)
  ordering = ('email',)
  filter_horizontal = ()


  fieldsets = (
    (None, {'fields': ('email', 'password')}),
    ("Personal Info", {'fields': ('nickname', 'profile_picture', 'gender', 'age', 'race', 'location')}),
    ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active')}),
  )

  add_fieldsets = (
    (None, {'classes': ('wide',),
    'fields': ('email', 'nickname', 'profile_picture', 'gender', 'age', 'race', 'location', 'password1', 'password2',)}),
  )


admin.site.unregister(Group)