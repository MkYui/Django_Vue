from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    """
    Blog Category
    """
    text = models.CharField(max_length=200, verbose_name="类别",)

    class Meta:
        verbose_name = '种类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text


class Article(models.Model):
    """
    Blog Article
    """
    title = models.CharField(max_length=250, verbose_name="标题")
    body = models.TextField(verbose_name="正文")
    author = models.ForeignKey(User, related_name="article", verbose_name="作者"
                                , on_delete=models.CASCADE,)
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新日期")
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, related_name="article", blank=True,
                    null=True, verbose_name="种类", on_delete=models.CASCADE,)

    class Meta:
        ordering = ('-updated',)
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])


class Comment(models.Model):
    """
    Blog Comment
    """
    article = models.ForeignKey(Article, related_name="comment", verbose_name="文章"
                                , on_delete=models.CASCADE,)
    content = models.CharField(max_length=250, verbose_name="内容")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")
    author = models.ForeignKey(User, related_name="comment", verbose_name="作者"
                                , on_delete=models.CASCADE,)

    class Meta:
        ordering = ('-created',)
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
