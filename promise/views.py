from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Count, F
from datetime import datetime
from promise.filters import PromiseFilter
from .models import *


# Create your views here.


# Create your views here.
class PromiseListView(generic.ListView):
    template_name = 'promise/list_all.html'
    context_object_name = 'promise_list_all'

    def get_queryset(self):
        return Promise.objects.all().order_by('-id')


class PromiseDetailView(generic.DetailView):
    model = Promise
    template_name = 'promise/detail.html'
    context_object_name = 'promise'


def search(request):
    promise_list = Promise.objects.all()
    promise_filter = PromiseFilter(request.GET, queryset=promise_list)
    return render(request, 'search/promise_list.html', {'filter': promise_filter})


def home(request):
    popular_promise_list = Promise.objects.annotate(rating=F('vote_up') + F('vote_down')).order_by('-rating')[:4]
    soonest_promise_list = \
        Promise.objects.filter(status__name='В процессе').filter(finish_date__gte=datetime.now()).order_by(
            'finish_date')[:4]
    newest_promise_list = Promise.objects.order_by('-id')[:4]

    first_popular_promise = popular_promise_list[0]
    first_soonest_promise = soonest_promise_list[0]
    first_newest_promise = newest_promise_list[0]

    context = {
        'first_popular_promise': first_popular_promise,
        'first_soonest_promise': first_soonest_promise,
        'first_newest_promise': first_newest_promise

    }
    return render(request, 'home/home.html', context)
