from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

from . import settings


urlpatterns = [    
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('user/', include('users.urls', namespace='user')),
    path('catalog/', include('goods.urls', namespace='catalog')),
    path('cart/', include('carts.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='order')),
    # Installs urls
    path('captcha/', include('captcha.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
