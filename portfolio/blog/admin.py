from django.contrib import admin
from blog.models import AboutMe,Education,Experience,Achivement,Title,Skill,Projects,Hobby
# Register your models here.
class AboutMeAdmin(admin.ModelAdmin):
    list_diaplsy=('about_me','photo')
admin.site.register(AboutMe)

class EducationAdmin(admin.ModelAdmin):
    list_diaplsy=('name','speci','colleg','marks')
admin.site.register(Education)

class ExperienceAdmin(admin.ModelAdmin):
    list_diaplsy=('name_o','post','type_j')
admin.site.register(Experience)

class AchivementAdmin(admin.ModelAdmin):
    list_diaplsy=('name_a','desc')
admin.site.register(Achivement)

class TitleAdmin(admin.ModelAdmin):
    list_diaplsy=('name','title')
admin.site.register(Title)

class SkillAdmin(admin.ModelAdmin):
    list_diaplsy=('name')
admin.site.register(Skill)

class ProjectsAdmin(admin.ModelAdmin):
    list_diaplsy=('title','s_date','e_date')
admin.site.register(Projects)

class HobbyAdmin(admin.ModelAdmin):
    list_diaplsy=('name')
admin.site.register(Hobby)
