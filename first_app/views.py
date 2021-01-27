# I have created this File Aman
import os
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name':'harry','place':'Mars'}
    return render(request,'index.html',params)
def analyze(request):
    djtext=request.POST.get('text','default')
    rp=request.POST.get('removepunc','off')
    params={}
    if rp == "on":
        punctuations='''~`!@#$%^&*()-_=+[]}{\|;':"<>?,./'''
        analyzed=""
        for index,i in enumerate(djtext):
            if i not  in punctuations:
                analyzed+=i
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze2.html',params) 
    nlremove=request.POST.get('nlremove',"off")
    if nlremove=="on":
        analyzed=""
        for i in djtext:
            if i!="\n":
                analyzed+=i
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze2.html',params)    
    
    capitalize=request.POST.get('capitalize',"off")
    if capitalize=="on":
        analyzed=""
        for i in djtext:
            analyzed+=i.upper()
        params={'purpose':'UPPERCASE','analyzed_text':analyzed}
        djtext=analyzed
    # else:
    #     return HttpResponse("Error")
    return render(request,'analyze2.html',params)    
    