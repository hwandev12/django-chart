from django.contrib import admin
from .models import Post, Expense, User, Line, Time

admin.site.register(Post)
admin.site.register(Expense)
admin.site.register(User)
admin.site.register(Line)
admin.site.register(Time)
