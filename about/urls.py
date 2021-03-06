from django.urls import path
from about import views
from django.conf.urls.static import static
from django.conf import settings

app_name ="about"

urlpatterns = [
    # https://.../about/
    path('', views.about_me, name='about')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
