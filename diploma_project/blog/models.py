from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    STATUS_VARIANT = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='ссылка')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices = STATUS_VARIANT, default='draft')


    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    
    class Meta:
        db_table = 'post'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-publish',)

    
    def __str__ (self):
        return self.title


# Create your models here.
