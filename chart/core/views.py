from django.shortcuts import render
from .models import Post, Expense, User


def home(request):
	posts = Post.objects.all()
	expenses = Expense.objects.all()
	users = User.objects.all()
	context = {
		"posts": posts,
		"expenses": expenses,
		"users": users
	}
	return render(request, 'blog/index.html', context)

# Piemarket
def pieMarket(request):
	posts = Post.objects.all()
	expenses = Expense.objects.all()
	users = User.objects.all()
	context = {
		"posts": posts,
		"expenses": expenses,
		"users": users
	}
	return render(request, 'blog/market-pie.html', context)

def line(request):
	return render(request, 'blog/line.html')
def bubble(request):
	return render(request, 'blog/bubble.html')
def flow(request):
	return render(request, 'blog/flow.html')
def diagram(request):
	return render(request, 'blog/diagram.html')
