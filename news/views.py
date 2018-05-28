from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404


def all_news(request):
    object_list = News.objects.all()
    paginator = Paginator(object_list, 2)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    context = {'all_news': news,
               'page': page}
    return render(request, 'all_news.html', context)


def article(request, news_id):
    detail = get_object_or_404(News, pk=news_id)
    return render(request, 'article.html', {'detail': detail})


def test(request, post_id):
    number = int(post_id)
    if number >= 0:
        contest = {'number': number}
        return render(request, 'test.html', contest)
