from django.db import models

from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class Language(models.Model):
    language_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.language_name

class Post(models.Model):
    post_name = models.CharField(max_length=255)
    post_category = models.ForeignKey(Category, related_name='post_category', on_delete=models.CASCADE)
    post_language = models.ForeignKey(Language, related_name='post_language', on_delete=models.CASCADE)
    
    def __str__(self):
       return self.post_name