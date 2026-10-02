
from django.contrib import admin
from django.urls import include, path
from blog.views import index

app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index')
]
