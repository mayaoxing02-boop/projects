from django.shortcuts import render

# Create your views here.
from .models import Article


def article_list(request):
    """
    视图函数：处理获取文章列表的请求
    """
    """从数据库中获取所有文字，并按照发布时间倒序排列"""
    articles =Article.objects.all().order_by('-publish_date')


    """
    将数据打包成字典形式，传给前端模板
    """
    context ={
        'articles': articles,
        'pahe_title':'星川皆无恙的大数据咨询站'


    }



    # 渲染并返回一个HTML模板
    #通过视图函数把函数取出来展示给用户
    return render(request,'articles/list.html',context)
