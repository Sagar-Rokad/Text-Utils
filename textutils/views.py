# I have created this File -- Sagar
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    if removepunc == 'on':
        analyzed = ''
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char

        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed+char
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if spaceremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != ' ':
                analyzed = analyzed+char
        params = {'purpose': 'Remove Spaces', 'analyzed_text': analyzed}

    if removepunc != 'on' and newlineremover != 'on' and spaceremover != 'on' and fullcaps != 'on':
        return HttpResponse("Please Select Any Operation And Try Again")

    return render(request, 'analyze.html', params)
