from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('courses', views.courses, name="courses"),
    path('blog', views.blog, name="blog"),
    path('contact', views.contact, name="contact"),
    path('sendmail', views.sendmail, name="sendmail"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


