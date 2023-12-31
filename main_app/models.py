from django.db import models
from django.urls import reverse
# Create your models here.
class Book(models.Model):
  name = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  year = models.IntegerField()

  def __str__(self):
    return f'{self.name} ({self.id})'
    
  def get_absolute_url(self):
    return reverse('detail', kwargs={'book_id': self.id})