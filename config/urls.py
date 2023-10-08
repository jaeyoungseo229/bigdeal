from django.contrib import admin
from django.urls import path, include

from bigdeal.views import base_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bigdeal/', include('bigdeal.urls')),
    #path('dist/', include('dist.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
]

#urlpatterns += static(settings.prod.STATIC_ROOT)

