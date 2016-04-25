from django.shortcuts import render

from webApp.models import SearchResult

a = SearchResult()
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            found = []
            found = a.phrasesearch(q)
            print found
            return render(request, 'search_results.html',
                {'results': found, 'query': q})
    return render(request, 'search_form.html',
        {'error': error})
