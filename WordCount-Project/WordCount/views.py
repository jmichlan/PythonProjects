from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fullText = request.GET['fullText']

    wordSplit = fullText.split()

    wordCount = {}
    for word in wordSplit:
        if word in wordCount:
            wordCount[word]+= 1

        else:
            wordCount[word]=1

    sortedWords= sorted(wordCount.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fullText':fullText, 'count': len(wordSplit),'sortedWords':sortedWords})

def about(request):
    return render(request, 'about.html')
