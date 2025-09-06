from django.contrib import admin

from .models import AuthorBook, Foods, Chefs, Category, Contact




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ('name', )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", 'email', 'subject')
    list_display_links = ('name', )

@admin.register(Foods)
class FoodsAdmin(admin.ModelAdmin):
    list_display = ("name", 'price')


@admin.register(AuthorBook)
class FoodsAdmin(admin.ModelAdmin):
    list_display = ("ism", 'familiya')
    list_display_links = ('familiya', )