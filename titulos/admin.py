from django.contrib import admin
from .models import Titulo, Sit


class Tituloadmin(admin.ModelAdmin):
    list_display = ('id', 'livro', 'autor', 'sit')
    list_display_links = ('id', 'livro', 'autor')
    list_per_page = 10
    search_fields= ('livro','autor','editora')

admin.site.register(Sit)
admin.site.register(Titulo, Tituloadmin)
# Register your models here.
