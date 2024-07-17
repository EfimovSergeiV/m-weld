from django.db import models
from django_resized import ResizedImageField
from mptt.models import MPTTModel, TreeForeignKey
from django_ckeditor_5.fields import CKEditor5Field



class CategoryModel(MPTTModel):
    """ Модель категории """

    activated = models.BooleanField(default=True, verbose_name='Активирован')
    parent = TreeForeignKey('self', verbose_name="Вложенность", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    name = models.CharField(max_length=255, verbose_name='Название')
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name



class ProductModel(models.Model):
    """ Мадель продукта """

    activated = models.BooleanField(default=True, verbose_name='Активирован')
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Категория')
    preview = ResizedImageField(size=[200, 200], quality=75, upload_to='prev/', verbose_name='Превью')
    name = models.CharField(max_length=255, verbose_name='Название')
    description = CKEditor5Field(verbose_name="Description",null=True, blank=True, config_name='extends')

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name