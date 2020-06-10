from django.db import models
from django.utils import timezone

# Create your models here.

class RankModel(models.Model):
    """
    排名模型类
    """
    rank_name = models.CharField(max_length=32, unique=True, verbose_name='客户端名称', blank=True, null=True)
    rank_score = models.IntegerField(verbose_name='分数', blank=True, null=True)

    class Meta:
        db_table = 'rank'
        verbose_name_plural = '排名'
