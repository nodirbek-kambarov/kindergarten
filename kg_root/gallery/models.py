from django.db import models


class Gallery(models.Model):
    photo = models.ImageField(upload_to='galimg')

    def __str__(self):
        self.name = 'Фотография'
        return self.name

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии галереи'
