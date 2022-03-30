from django.shortcuts import render
from .models import Post, Expense, User, Line, Time


def home(request):
    posts = Post.objects.all()
    expenses = Expense.objects.all()
    users = User.objects.all()
    context = {"posts": posts, "expenses": expenses, "users": users}
    return render(request, 'blog/index.html', context)


# Piemarket
def pieMarket(request):
    posts = Post.objects.all()
    expenses = Expense.objects.all()
    users = User.objects.all()
    context = {"posts": posts, "expenses": expenses, "users": users}
    return render(request, 'blog/market-pie.html', context)


def line(request):
    lines = Line.objects.all()
    context = {"lines": lines}
    return render(request, 'blog/line.html', context)


def bubble(request):
    times = Time.objects.all()
    context = {"times": times}
    return render(request, 'blog/bubble.html', context)


def flow(request):
    return render(request, 'blog/flow.html')


def diagram(request):
    return render(request, 'blog/diagram.html')
