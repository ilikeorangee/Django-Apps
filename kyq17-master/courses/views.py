from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from courses.models import Language, Course, Content
# Create your views here.
def home(request):
	language = Language.objects.all()
	course = Course.objects.all().order_by('name')
	content = Content.objects.all().order_by("-date")
	paginator = Paginator(content, 6)
	page = request.GET.get('page') 
	content = paginator.get_page(page)
	content_dict = {
		'language':language,
		'course': course,
		'content':content,
		'paginator':paginator
	}
	
	return render(request, 'course/home.html', content_dict)

def language_pg(request, slug):
	all_lang = Language.objects.all().order_by('name')
	language = get_object_or_404(Language, slug=slug)
	all_course = Course.objects.all().order_by('name')
	course = Course.objects.filter(language=language).order_by("date")
	content = Content.objects.filter(language=language).order_by("-date")
	paginator = Paginator(content, 6)
	page = request.GET.get('page') 
	content = paginator.get_page(page)

	content_dict = {
		'all_lang':all_lang,
		'all_course':all_course,
		'language':language,
		'course':course,
		'content':content,
		'paginator':paginator
	}
	
	return render(request, 'course/language.html', content_dict)

def course_pg(request, slug):
	all_lang = Language.objects.all().order_by('name')
	all_course = Course.objects.all().order_by('name')

	course = get_object_or_404(Course, slug=slug)
	content = Content.objects.filter(course=course).order_by("-date")
	paginator = Paginator(content, 6)
	page = request.GET.get('page') 
	content = paginator.get_page(page)

	content_dict = {
		'all_lang':all_lang,
		'all_course':all_course,
		'course':course,
		'content':content,
		'paginator':paginator

	}
	return render(request, 'course/course.html', content_dict)


def content_pg(request, slug):
	all_course = Course.objects.all().order_by('name')
	all_lang = Language.objects.all().order_by('name')
	content = Content.objects.get(slug=slug)

	content_dict = {
		'content':content,
		'all_lang':all_lang,
		'all_course':all_course
	}
	return render(request, 'course/content.html', content_dict)

def tostart(request):
	language = Language.objects.all()
	course = Course.objects.all().order_by('name')
	content = Content.objects.all().order_by("date")
	content_dict = {
		'language':language,
		'course': course,
		'content':content,
		
	}
	
	return render(request, 'course/tostart.html', content_dict)

def msg(request):
	
	return render(request, 'course/msg.html')

