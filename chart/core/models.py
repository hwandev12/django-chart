from django.db import models


class Post(models.Model):

	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "My posts"

	name = models.CharField(max_length=50)
	quantity = models.IntegerField()

	def __str__(self):
		return self.name
