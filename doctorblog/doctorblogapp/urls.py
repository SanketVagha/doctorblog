from django.urls import path, include
from doctorblogapp import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.index, name= "index"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
    path('doctorBlog', views.doctorBlog, name="doctorBlog"),
    path('add', views.add, name="add"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete")
]

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, documents_root = settings.MEDIA_ROOT)