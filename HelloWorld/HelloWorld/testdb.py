# -- coding: utf-8 --

from django.http import HttpResponse
from TestModel.models import Test


def add(request):
	# 创建数据库
	test1 = Test(name='test')
	test1.save()
	return HttpResponse('<p>数据添加成功!</p>')


def query(request):
	# 初始化
	response = ""
	response1 = ""

	# 通过objects这个模型管理器的all()获取所有数据行，相当于SQL中的select * from 
	list = Test.objects.all()

	# filter相当于sql中的where,可设置条件过滤结果
	response2 = Test.objects.filter(id=1)

	# 获取单个对象
	response3 = Test.objects.get(id=1)

	# 限制返回的数据 相当于sql中的offset 0 limit 2;
	Test.objects.order_by('name')[0:2]

	# 数据排序
	Test.objects.order_by('id')

	# 上面的方法可以连锁使用
	Test.objects.filter(name='test').order_by('id')

	# 输出所有数据
	for var in list:
		response1 += var.name + " "
	response = response1
	return HttpResponse("<p>" + response + "</p>")


def update(request):
	# 修改其中一个id=1的name字段，再save，相当于sql中的update
	test1 = Test.objects.get(id = 1)
	test1.name = 'Google'
	test1.save()

	# 另一种方式
	#Test.objects.filter(id=1).update(name='First Blood')

	# 修改所有的列
	#Test.objects.all().update(name='Fuck you')

	return HttpResponse("<p>修改成功</p>")


def delete(request):
	# 删除id=2的数据
	test1 = Test.objects.filter(id = 2)
	if test1:
		test1.delete()

	# 另一种方式
	#Test.objects.filter(id = 2).delete()

	# 删除所有数据
	#Test.objects.all().delete()

	return HttpResponse("<p>删除成功</p>")
