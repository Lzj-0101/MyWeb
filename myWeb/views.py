from django.http import HttpResponse
from django.shortcuts import render

POST_FORM = '''
<form method='post' action='/test_get_post'>
    用户名:<input type='text' name='username'>
    <input type='submit' value='提交'>
</form>

'''


def page_1(request):
    html = '<h1>the first page</h1>'
    return HttpResponse(html)


def page_n(request, num):
    if num in [n for n in range(2, 101)]:
        html = '<h1>the page %s</h1>' % (num)
        return HttpResponse(html)
    else:
        return HttpResponse('no page')


def cal_1(request, x, op, y):
    if op not in ['add', 'sub', 'mul', 'dev']:
        return HttpResponse('op is invalid')
    x = int(x)
    y = int(y)
    result = 0
    if op == 'add':
        result = x + y
    elif op == 'sub':
        result = x - y
    elif op == 'mul':
        result = x * y
    elif op == 'dev':
        result = x / y

    return HttpResponse('result is %s and op is %s' % (result, op))


def cal_2(request, n, op, m):
    if op not in ['add', 'sub', 'mul', 'dev']:
        return HttpResponse('op is invalid')

    result = 0
    if op == 'add':
        result = n + m
    elif op == 'sub':
        result = n - m
    elif op == 'mul':
        result = n * m
    elif op == 'dev':
        result = n / m
    return HttpResponse('result is %s' % (result))


def test_request(request):
    print('path info is ', request.path_info)
    print('method is ', request.method)
    print(request.GET['a'])

    return HttpResponse('test request is ok')


def test_get_post(request):
    if request.method == 'GET':
        # print(request.GET)
        # print(request.GET['a'])
        # print(request.GET.get('b','no such a word'))
        # print(request.GET.getlist('a'))

        return HttpResponse(POST_FORM)
    elif request.method == 'POST':
        print('username is', request.POST['username'])
        return HttpResponse('post ok')
    else:
        return HttpResponse(POST_FORM)


'''
模板中使用变量语法
    {{变量名}}
    {{变量名.index}}    --索引
    {{变量名.key}}  --字典中的值
    {{对象.方法}}
    {{函数名}}

模板标签
    {% 标签 %}
    ···
    {% 结束标签 %}
'''


def test_template_html(request):
    '''
    render(request,'模板文件名(带后缀)',字典类型的数据)
    视图函数将python变量封装到字典类型的数据中,传递到模板中
    模板中使用 {{变量名}} 的语法调用视图函数传进来的变量
    '''
    # 第一种方法
    # from django.template import loader
    # t = loader.get_template('test_html.html')
    # html = t.render()
    # return HttpResponse(html)
    # 第二种方法
    from django.shortcuts import render
    test_dict = {
        'int': 88, 'str': 'lizijian', 'list': ['a', 'b', 'c'],
        'dict': {'adc': 1, 'mt': 'we'}, 'func': say_hi, 'class_obj': Dog()
    }
    return render(request, 'test_html.html', test_dict)


def say_hi():
    print('hi!')
    return 'hello!'


class Dog:
    def woof(self):
        print('www')
        return 'wang'


def test_if_for(request):
    test_dict = {}
    test_dict['x'] = 10
    test_dict['y'] = 29
    return render(request, 'test_if_for.html', test_dict)


def test_cal(request):
    if request.method == 'GET':
        return render(request, "test_cal.html")
    elif request.method == 'POST':
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']

        result = 0
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'dev':
            result = x / y

# locals()  可以生成函数内部局部变量的字典
# 在本函数中 即 locals() 相等于 dict = {'x':x,'y':y,'op':op}
        return render(request, 'test_cal.html', locals())
