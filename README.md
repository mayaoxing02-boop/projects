# Django_极简大数据资讯管理系统

#### 项目介绍
基于 Python + Django 构建的轻量级大数据资讯管理系统，面向零基础学习者的 Django 实战项目。
核心目标：通过极简的代码实现「文章数据管理」全流程，掌握 Django MTV 架构、ORM 数据库操作、Admin 后台配置等核心知识点。
技术栈：Python 3.9 + Django 4.2 + SQLite + HTML/CSS

#### 软件架构
采用 Django 经典 MTV 架构：
- **M (Model)**：数据模型层，负责与 SQLite 数据库交互，定义文章表结构（标题、作者、内容、发布时间、阅读量）；
- **T (Template)**：模板层，负责前端页面渲染，通过 Django 模板语言展示文章列表；
- **V (View)**：视图层，核心业务逻辑层，处理 HTTP 请求、从数据库获取数据并传递给模板。

#### 安装教程
1. **环境准备**
   - 安装 Python 3.9（推荐 3.9.x 版本）：https://www.python.org/downloads/release/python-390/
   - 验证安装：终端执行 `python --version`，显示 3.9.x 即成功。

2. **创建虚拟环境（推荐）**
   ```bash
   # 进入项目根目录（manage.py 所在目录）
   cd 你的项目路径/Django_极简大数据资讯管理系统
   # 创建虚拟环境
   python -3.9 -m venv venv
   # 激活虚拟环境（Windows）
   venv\Scripts\activate
   # 激活虚拟环境（macOS/Linux）
   source venv/bin/activate


# 安装 Django 4.2 稳定版
pip install django==4.2.*
# 验证安装：终端执行 python -m django --version，显示 4.2.x 即成功

# 生成迁移文件（将模型转换为数据库表结构）
python manage.py makemigrations
# 执行迁移（创建数据库表）
python manage.py migrate

python manage.py createsuperuser
# 按提示输入用户名、邮箱、密码（密码输入时不可见，正常输入即可）

python manage.py runserver
# 终端显示 "Starting development server at http://127.0.0.1:8000/" 即启动成功

使用说明
访问前端页面
浏览器打开：http://127.0.0.1:8000/articles/
初始无数据时显示「暂时还没有发布任何文章哦～」，需先在后台添加文章。
访问 Admin 后台管理
浏览器打开：http://127.0.0.1:8000/admin/
输入步骤 5 创建的超级管理员账号密码，进入后台。
点击「科技文章」→「添加」，录入文章标题、作者、内容等信息，保存后前端页面会自动显示。
核心功能操作
新增文章：Admin 后台「科技文章」→「添加」；
修改 / 删除文章：Admin 后台文章列表页点击对应文章操作；
查看文章列表：前端 http://127.0.0.1:8000/articles/ 自动按发布时间倒序展示。

