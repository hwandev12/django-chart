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
