from django.urls import path
from rest_noticia.views import lista_noticias, detalle_noticia
from rest_noticia.viewsLogin import login

urlpatterns = [
    path('lista_noticias', lista_noticias, name="lista_noticias"),
    path('detalle_noticia/<id>', detalle_noticia, name="detalle_noticia"),
    path('login',login, name="login"),
]
