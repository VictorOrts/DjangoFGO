from django.contrib import admin
from .models import Character,Skill,Character_class
# Register your models here.

admin.site.register(Character)
admin.site.register(Character_class)
admin.site.register(Skill)