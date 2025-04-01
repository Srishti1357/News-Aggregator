from django.db import models

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('home', 'Home'),
        ('business', 'Business'),
        ('entertainment', 'Entertainment'),
        ('health', 'Health'),
        ('science', 'Science'),
        ('sports', 'Sports'),
        ('technology', 'Technology'),    
    ]
    
    title = models.CharField(max_length=255)  # Title of the news article
    link = models.URLField()  # URL link to the news article
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the article was created
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES,default='general')# Category of the article
    date = models.DateField( null=True, blank=True)
    # publisher_name = models.CharField(max_length=255, null=True, blank=True)
    publisher_logo = models.URLField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    lastmod = models.DateTimeField(null=True, blank=True)

    

    def __str__(self):
        return self.title

