from django.db import models
from django.utils import timezone

class User(models.Model):
	nickname = models.CharField(max_length=50)
	date_joined = models.DateTimeField(default=timezone.now)
	groups = models.ManyToManyField('Group', related_name='users')

	def __str__(self):
		return self.nickname

class Group(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(default="Default Description")
	members = models.ManyToManyField(User, through='Together')

	def __str__(self):
		return self.name

class Together(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
