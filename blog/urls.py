from django.urls import path 
from blog.views import home, form_post, form_mod_post, form_del_post, tienda, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, log_in
from django.views.generic import TemplateView


urlpatterns = [
    path('',home,name='home'),
    path('form_post',form_post,name='form_post'),
    path('form_mod_post/<id>',form_mod_post,name='form_mod_post'),
    path('form_del_post/<id>',form_del_post,name='form_del_post'),
    path('log_in',log_in,name='log_in'),

    path('tienda',tienda,name='tienda'),
    path('agregar/<int:producto_id>', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="Cls"),

    



]