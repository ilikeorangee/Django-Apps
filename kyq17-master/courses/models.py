from django.db import models
from embed_video.fields import EmbedVideoField


def get_image_path_series(instance, filename):
	return '/'.join([''])

class Language(models.Model):
	name = models.CharField(max_length=128, unique=True)
	descritpion = models.TextField()
	source_title = models.TextField()
	source = models.URLField(blank=True, null=True)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to='get_image_path_series', blank=True, null=True)

	source_title = models.TextField()
	source = models.URLField(blank=True, null=True)
	
	source_title1 = models.TextField()
	source1 = models.URLField(blank=True, null=True)

	source_title2 = models.TextField()
	source2 = models.URLField(blank=True, null=True)

	source_title3 = models.TextField()
	source3 = models.URLField(blank=True, null=True)

	source_title4 = models.TextField()
	source4 = models.URLField(blank=True, null=True)

	def __str__(self):
		return self.name

def get_image_path_season(instance, filename):
	return '/'.join([''])	

class Course(models.Model):
	language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
	date = models.DateTimeField(auto_now_add = True)
	name = models.CharField(max_length=128, unique=True)
	source = models.URLField(blank=True, null=True)
	description = models.TextField()
	rate = models.IntegerField(default=1)	
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to='get_image_path_season', blank=True, null=True)				

	def __str__(self):
		return str(self.name)


def get_image_path(instance, filename):
	return '/'.join([''])	

def get_image_path_note(instance, filename):
	return '/'.join([''])		

class Content(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=128)
	summary_question = models.TextField()
	description = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	image = models.ImageField(upload_to='get_image_path', blank=True, null=True)
	slug = models.SlugField(unique=True)
	language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
	review = models.TextField()
	video = EmbedVideoField(blank=True, null=True)	

	pdf = models.URLField(blank=True, null=True)
	github = models.URLField(blank=True, null=True)
	paper_work = models.URLField(blank=True, null=True)



	def __str__(self):
		return self.title



