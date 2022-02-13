from django.http import HttpResponse


POST_FORM = '''
<form method='post' action='/test_get_post'>
    用户名:<input type='text' name='username'>
    <input type='submit' value='提交'>
</form>

'''

def page_1(request):
    html = '<h1>the first page</h1>'
    return HttpResponse(html)

def page_n(request,num):
    if num in [n for n in range(2,101)]:
        html = '<h1>the page %s</h1>'%(num)
        return HttpResponse(html)
    else:
        return HttpResponse('no page')

def cal_1(request,x,op,y):
    if op not in ['add','sub','mul','dev']:
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

    return HttpResponse('result is %s and op is %s'%(result,op))

def cal_2(request,n,op,m):
    if op not in ['add','sub','mul','dev']:
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
    return HttpResponse('result is %s'%(result))

def test_request(request):
    print('path info is ',request.path_info)
    print('method is ',request.method)
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
        print('username is',request.POST['username'])
        return HttpResponse('post ok')
    else:
        return HttpResponse(POST_FORM)

def test_html(request):
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
    test_dict = {'username':'LZJ'}
    return render(request,'test_html.html',test_dict)
