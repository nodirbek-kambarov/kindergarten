from django.db import models


class Workers(models.Model):
    workers_photo = models.ImageField(upload_to='workersimg')
    workers_name = models.CharField(max_length=255)
    workers_position = models.CharField(max_length=50, null=True, default='Учитель')

    def __str__(self):
        return self.workers_name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
