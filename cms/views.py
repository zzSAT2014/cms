from django.shortcuts import render


def tryhtmlresponse(request):

    print request.POST
    return render(request, 'fun/tryhtml.html', {})


def tryhtml(request):
    return render(request, 'fun/tryhtml.html', {})
