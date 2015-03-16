from django.db import models

# Create your models here.

class Genre(models.Model):
	genre = models.CharField(max_length=50)
	'''
	genre2 = models.CharField(max_length=50)
	genre3 = models.CharField(max_length=50)
	genre4 = models.CharField(max_length=50)
	genre5 = models.CharField(max_length=50)
	genre6 = models.CharField(max_length=50)
	genre7 = models.CharField(max_length=50)
	genre8 = models.CharField(max_length=50)
	genre9 = models.CharField(max_length=50)
	genre10 = models.CharField(max_length=50)
	'''
	
	def __str__(self):
	    return unicode(self.genre)


class Game(models.Model):
	name = models.CharField(max_length=100)
	link_to_image = models.CharField(max_length=1000)
	tag1 = models.ForeignKey(Genre, related_name="description1")
	tag2 = models.ForeignKey(Genre, related_name="description2")
	'''
	tag3 = models.ForeignKey(Genre)
	tag4 = models.ForeignKey(Genre)
	tag5 = models.ForeignKey(Genre)
	'''
	def __str__(self):
		return self.name

