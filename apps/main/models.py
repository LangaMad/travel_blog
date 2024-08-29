from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    image = models.ImageField('Картинка', upload_to='about_us')
    text1 = models.TextField('Текст 1')
    title2 = models.CharField('Почему мы', max_length=50)
    text2 = models.TextField('Почему мы текст')
    title3 = models.CharField('Наши преимущества', max_length=50)
    text3 = models.TextField('Преимущества текст')
    title4 = models.CharField('Наши услуги', max_length=50)
    text4 = models.TextField('Услуги текст')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О насы'


class ContactUs(models.Model):
    name = models.CharField('Имя', max_length=50)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=50)
    message = models.TextField('Сообщение')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

