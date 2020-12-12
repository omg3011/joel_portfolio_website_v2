from django.urls import path
from portfolio import views
from django.conf.urls.static import static
from django.conf import settings

app_name ="portfolio"

urlpatterns = [
    # https://.../about/
    path('', views.categories, name='categories')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
