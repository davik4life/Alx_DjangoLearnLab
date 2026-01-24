from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser


# Register your models here.
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ("title", "author", "publication_year")
#     list_filter = ("author", "publication_year")
#     search_fields = ("title", "author")
#     admin.site.register = ("CustomUser", "CustomUserAdmin")



# class CustomUser(UserAdmin):
#     model = CustomUser

#     fieldsets = UserAdmin.fieldsets + (
#         ("Additional Information", {
#             "fields": ("date_of_birth", "profile_photo")
#         }),
#     )

#     add_fieldsets = UserAdmin.add_fieldsets + (
#         ("Additional Information", {
#             "fields": ("date_of_birth", "profile_photo")
#         }),
#     )

#     list_display = (
#         "username",
#         "email",
#         "first_name",
#         "last_name",
#         "is_staff",
#         "date_of_birth",
#     )

# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     pass



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)
    ordering = ("id",)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    class Meta:
        permissions = [
            ("can_create", "Can create objects"),
            ("can_delete", "Can delete objects"),
        ]
    model = CustomUser


# admin.site.register(Book)
# # admin.site.register(CustomUser, UserAdmin)
# admin.site.register(CustomUser, CustomUserAdmin)