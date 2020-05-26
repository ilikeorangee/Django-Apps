from django.contrib import admin

# import your model
from courses.models import Language, Course, Content
# set up automated slug creation
class LanguageAdmin(admin.ModelAdmin):
    model = Language
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
# and register it
admin.site.register(Language, LanguageAdmin)

class CourseAdmin(admin.ModelAdmin):
	model = Course
	list_display = ('name', 'language')
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Course, CourseAdmin)


class ContentAdmin(admin.ModelAdmin):
	model = Content
	list_display = ('title', 'language', 'course')
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Content, ContentAdmin)



