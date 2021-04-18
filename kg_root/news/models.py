from django.db import models


class News(models.Model):
    news_photo = models.ImageField(upload_to='newsimg', default='-')
    news_title = models.CharField(max_length=255, null=False)
    news_text = models.TextField(default='Текст')
    news_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

