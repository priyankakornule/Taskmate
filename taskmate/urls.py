from django.contrib import admin
from django.urls import path, include
from todolist_app import views
#from users_app import views as users_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('task/', include('todolist_app.urls')),
    path('todolist/', include('todolist_app.urls')),
     path('account/', include('users_app.urls')),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]
