from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата и время публикации')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'           
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        verbose_name='Местоположение',
        null=True,
        blank=True       
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        null=True     
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)


class Category(models.Model):
    title = models.CharField('Заголовок', max_length=256)
    description = models.TextField('Описание')
    slug = models.SlugField('Идентификатор', unique=True)
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)


class Location(models.Model):
    name = models.CharField('Заголовок', max_length=256)
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)
