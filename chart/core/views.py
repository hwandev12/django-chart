from django.shortcuts import render
from .models import Post, Expense


def home(request):
	posts = Post.objects.all()
	expenses = Expense.objects.all()
	context = {
		"posts": posts,
		"expenses": expenses
	}
	return render(request, 'blog/index.html', context)

# Piemarket
def pieMarket(request):
	posts = Post.objects.all()
	context = {
		"posts": posts
	}
	return render(request, 'blog/market-pie.html', context)

def steps(request):
	posts = Post.objects.all()
	context = {
		"posts": posts
	}
	return render(request, 'blog/steps.html', context)
