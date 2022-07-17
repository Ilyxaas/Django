from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
   title = models.CharField(max_length=255, verbose_name='Заголовок')
   slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
   content = models.TextField(blank=True, verbose_name='Содержание')
   photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фото')
   time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
   time_update = models.DateTimeField(auto_now=True, verbose_name='Последнее редактирование')
   is_published = models.BooleanField(default=True, verbose_name='Опубликованно')
   likes = models.IntegerField(default=0, verbose_name='Лайки')
   dislikes = models.IntegerField(default=0, verbose_name='Дизлайки')
   Cat = models.ForeignKey('Category', on_delete=models.PROTECT)


   def __str__(self):
      return self.title

   def get_absolute_url(self):
      return reverse('post', kwargs={'post_slug': self.slug})

   class Meta:
      verbose_name = 'Пост'
      verbose_name_plural = 'Посты'
      ordering = ['time_create', 'likes', 'title']

class Category(models.Model):
   name = models.CharField(max_length=255, db_index=True, verbose_name='Название')
   slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

   def __str__(self):
      return self.name

   def get_absolute_url(self):
      return reverse('category', kwargs={'cat_slug': self.slug})

   class Meta:
      verbose_name = 'Категория'
      verbose_name_plural = 'Категории'
