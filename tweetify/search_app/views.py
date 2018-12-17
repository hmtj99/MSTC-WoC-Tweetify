from django.shortcuts import render
from search_app.forms import SearchForm

from search_app.forms import SearchForm

def index(request):
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            print("Topic is",search)
    return render(request,"search_app/index.html",{'form':form})
