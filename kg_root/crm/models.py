from django.db import models


class Order(models.Model):
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=26, verbose_name='Телефон')
    order_text = models.TextField(default=None, verbose_name='Текст')
    order_dt = models.DateField(auto_now=True)

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
