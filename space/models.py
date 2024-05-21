from django.db import models
from filer.fields.image import FilerImageField

# Create your models here.
class SlideImg(models.Model):
    img = FilerImageField(null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Фотографию для карусели'
        verbose_name_plural = 'Добавить фотографии в карусель'
        ordering = ['img']

    def __str__(self):
        return f'{self.img.url}'