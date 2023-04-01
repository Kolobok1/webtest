from django.db import models

class Articles(models.Model):
    title = models.CharField('Название теста', max_length=50)
    question = models.CharField('Вопрос', max_length=250)
    answer = models.CharField('Ответ', max_length=100)
    option = models.CharField('Вариант', max_length=100)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'