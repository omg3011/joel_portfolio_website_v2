from django.urls import path
from about import views

app_name ="about"

urlpatterns = [
    # https://.../about/
    path('', views.about_me, name='about')
]
