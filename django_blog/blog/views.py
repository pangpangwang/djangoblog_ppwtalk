from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from models import Category, Article
from django.shortcuts import render_to_response
import calendar, datetime

# Create your views here.
def home(request):
    return render(request, "blog/article/home.html")

def index(request) :
    """The news index"""
    archive_dates = Article.objects.dates('date_publish','month', order='DESC')
    categories = Category.objects.all()

    page = request.GET.get('page')
    article_queryset = Article.objects.all()
    paginator = Paginator(article_queryset, 10)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    return render(
        request,
        "blog/article/index.html",
        {
            "articles" : articles,
            "archive_dates" : archive_dates,
            "categories" : categories
        }
    )

def single(request, slug) :
    """A single article"""
    article = get_object_or_404(Article, slug=slug)
    article.visit = article.visit + 1
    article.save()
    archive_dates = Article.objects.dates('date_publish','month', order='DESC')
    categories = Category.objects.all()
    
    return render(
        request,
        "blog/article/single.html",
        {
            "article" : article,
            "archive_dates" : archive_dates,
            "categories" : categories
        }
    )
def likes(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.likes = article.likes + 1
    article.save()
    archive_dates = Article.objects.dates('date_publish','month', order='DESC')
    categories = Category.objects.all()    
    return render(
        request,
        "blog/article/single.html", 
         {
            "article" : article,
            "archive_dates" : archive_dates,
            "categories" : categories
        }
    )

def date_archive(request, year, month) :
    """The blog date archive"""
    # this archive pages dates
    year = int(year)
    month = int(month)
    month_range = calendar.monthrange(year, month)
    start = datetime.datetime(year=year, month=month,day=1)#.replace(tzinfo=utc)
    end = datetime.datetime(year=year, month=month, day=month_range[1])#.replace(tzinfo=utc)
    archive_dates = Article.objects.dates('date_publish','month', order='DESC')
    categories = Category.objects.all()

    # Pagination
    page = request.GET.get('page')
    article_queryset = Article.objects.filter(date_publish__range=(start.date(), end.date()))
    paginator = Paginator(article_queryset, 10)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    return render(
        request,
        "blog/article/date_archive.html",
        {
            "start" : start,
            "end" : end,
            "articles" : articles,
            "archive_dates" : archive_dates,
            "categories" : categories
        }
    )

def category_archive(request, slug):
    archive_dates = Article.objects.dates('date_publish','month', order='DESC')
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)

    # Pagination
    page = request.GET.get('page')
    article_queryset = Article.objects.filter(categories=category)
    paginator = Paginator(article_queryset, 10)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    return render(
        request,
        "blog/article/category_archive.html",
        {
            "articles" : articles,
            "archive_dates" : archive_dates,
            "categories" : categories,
            "category" : category
        }
    )

def about(request):
    return render(
        request,
        "about.html"
    )