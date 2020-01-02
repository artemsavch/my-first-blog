import datetime
from django.db import models
from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField('Name of the Article', max_length=200)
    article_text = models.TextField('Text of the Article')
    publishing_date = models.DateTimeField('Date of the Publishing')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.publishing_date >= (timezone.now() - datetime.timedelta(days=7))


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Author name', max_length=50)
    comment_text = models.CharField('Text of the comment', max_length=200)

    def __str__(self):
        return self.author_name
