from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import CategoryModel, ProductModel



class CategoryModelAdmin(MPTTModelAdmin):
    """ Категории """
    list_display = ('name', 'parent', 'activated')
    list_filter = ('activated', 'parent')
    search_fields = ('name', 'parent')
    mptt_level_indent = 20
    mptt_indent_field = "name"
    mptt_level_indicator = "name"
    mptt_tree_auto_open = 0


class ProductModelAdmin(admin.ModelAdmin):
    """ Продукты """
    list_display = ('name', 'category', 'activated')
    list_filter = ('activated', 'category')
    search_fields = ('name', 'category')


admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(ProductModel, ProductModelAdmin)