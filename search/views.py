from django.shortcuts import render

from django.contrib.flatpages.models import FlatPage
from django.http import HttpResponseRedirect
# Create your views here.


def search(request):
    q = request.GET.get('q', '')
    result = []
    keyresult = []
    if q:
        result = FlatPage.objects.filter(content__icontains=q)
        keyresult = FlatPage.objects.filter(searchkeyword__keyword__in=q.split()).distinct()
        if result.count() == 1:
            page = result[0]
            print page
            print page.get_absolute_url()
            return HttpResponseRedirect(page.get_absolute_url())
    print result
    return render(request, 'search/search.html', {'query': q, 'result': result, 'keyresult': keyresult})
