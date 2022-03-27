from django.shortcuts import render
from .models import Post

def home(request):
	posts = Post.objects.all()
	context = {
		"posts": posts
	}
	return render(request, 'blog/index.html', context)

# Piemarket
def pieMarket(request):
	return render(request, 'blog/market-pie.html')
