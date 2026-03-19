from django.db import models

# Create your models here.
class Article(models.Model):
    ##models.Model是Django所有数据模型的“基类 （父类）”
    """文章数据模型：定义数据库中的表结构"""
    """author：字段名，对应数据库中的列名
    models包含所有数据库字段类型
    CharField：字符串字段类型，用于存储文本
    max_length = 50指定字符的最大字符长度
    verbose_后台显示的字段名称
    """
    title = models.CharField(max_length=200,verbose_name="文章标题")
    author = models.CharField(max_length=50,verbose_name="作者")
    content = models.TextField(verbose_name="正文内容")
    publish_date = models.DateTimeField(auto_now_add=True,verbose_name="发布时间")
    views = models.IntegerField(default=0,verbose_name="阅读量")

    def __str__(self):
      """"用文章标题作为对象的「显示名」"""
      #改备注
      return self.title


    class Meta:
        #分类
        verbose_name="科技文章"
        verbose_name_plural="科技文章"

