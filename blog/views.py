from django.shortcuts import render, redirect, HttpResponse
from .models import BlogPost, Producto
from .forms import PostForm 
from .Carrito import Carrito

# Create your views here.



def home(request):
    post = BlogPost.objects.all()
    datos = {
        'post':post
    }
    return render(request, 'blog/Index.html',datos) 


#def form_post(request):
#    form= PostForm()
#    return render(request,'blog/form_noticia.html',{'form':form})

def form_post(request):
    posts = BlogPost.objects.all()
    datos = {
        'form':PostForm(),
        'post':posts
    }
    if(request.method == 'POST'):
        formulario = PostForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardados correctamente'
    return render(request,'blog/form_noticia.html',datos)



def form_mod_post(request, id):
    post = BlogPost.objects.get(title=id)
    posts = BlogPost.objects.all()
    datos = {
        'form':PostForm(instance=post),
        'post':posts
    }
    if(request.method=='POST'):
        formulario = PostForm(data=request.POST, instance=post)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modificados correctamente'

    return render(request,'blog/form_mod_noticia.html',datos)


def form_del_post(request, id):
    post = BlogPost.objects.get(title=id)
    post.delete()

    return redirect(to='home')



class Cliente:
    def __init__(self, rut, nombre, edad):
        self.rut = rut      
        self.nombre = nombre
        self.edad = edad
        super().__init__()




def hom(request):
    post = BlogPost.objects.all()
    datos = {
        'post':post
    }
    return render(request,'blog/Index.html')



def tienda(request):
    productos = Producto.objects.all()
    return render(request, "blog/tienda.html", {'productos':productos})


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("tienda")


def eliminar_producto(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("tienda")


def restar_producto(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")



def log_in(request):
    return render(request, "blog/login.html")