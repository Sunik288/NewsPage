from django.db import models

class NewsCategory(models.Model):
    category_name = models.CharField(max_length=32)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.category_name)

class News(models.Model):
    title = models.CharField(max_length=256)
    main_text = models.TextField()
    news_image = models.ImageField(blank=True)
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

