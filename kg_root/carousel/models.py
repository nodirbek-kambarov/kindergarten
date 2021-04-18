from django.db import models


class Carousel(models.Model):
    carousel_img = models.ImageField(upload_to='sliderimg')
    carousel_css = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS')

    def __str__(self):
        self.name = 'Фотографии'
        return self.name

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
