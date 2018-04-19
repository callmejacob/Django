# Django

使用Django框架搭建的服务器工程，Django使用参考官方文档: http://django-chinese-docs.readthedocs.org/

静态文件配置：
1. app目录下建立子目录static
2. 在settings.py中添加STATIC_ROOT = os.path.join(BASE_DIR, 'static')
3. 在html中使用相对路径引用static
