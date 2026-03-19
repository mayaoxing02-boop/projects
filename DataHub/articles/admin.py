from django.contrib import admin

# Register your models here.
from django.contrib import admin


from .models import  Article

"""
注册我们的Article模型
"""

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    配置在后台列表页显示的字段
    """
    list_display =('title','author','publish_date','views')

    """
    增加搜索功能
    """
    search_fields =('title','author')