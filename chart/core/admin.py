from django.contrib import admin
from .models import Post, Expense, User, Line

admin.site.register(Post)
admin.site.register(Expense)
admin.site.register(User)
admin.site.register(Line)
