#I have created this file-Jayesh

from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('''<h1>hello</h1>  <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django CodewithHaryy </a>''')
#
# def about(request):
#     return HttpResponse('hello about')

def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home <a href='/spaceremove'>Back</a>"

def analyze(request):
    global analyzed
    djtext=request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc', 'off')
    capitalall=request.POST.get('capitalall', 'off')
    removeextraspaces=request.POST.get('removeextraspaces', 'off')
    countcharacters=request.POST.get('countcharacters', 'off')


    count=0
    punctuations= '''!@#$%^&*()_:"<>,.;'?/{}[]|\+=-'''

    if (removepunc != "on" and removeextraspaces != "on" and countcharacters != "on" and capitalall != "on"):
        return HttpResponse("ERROR ! Please select any of the options")

    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed

    if (removeextraspaces == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                analyzed = analyzed + char
        djtext = analyzed

    if (countcharacters == "on"):
        for char in djtext:
            count=count+1
        djtext=analyzed

    if (capitalall == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
    if(countcharacters!="on"):
        params = {'Purpose': 'Analyzed Text', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    params = {'Purpose': 'Analyzed Text', 'analyzed_text': analyzed,'counting': count}
    return render(request, 'analyze.html', params)





    # print(djtext)

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newlineremove")
#
# def spaceremove(request):
#     return HttpResponse("spaceremove <a href='/'>Back</a>")
#
# def charcount(request):
#     return HttpResponse("charcount")