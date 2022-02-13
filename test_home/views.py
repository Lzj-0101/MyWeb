from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def test_index_view(request):
    # t = loader.get_template('index.html')
    # html = t.render()
    # return HttpResponse(html)
    return render(request,'index.html')