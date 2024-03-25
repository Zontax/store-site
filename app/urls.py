from app import settings
from app import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path


urlpatterns = [    
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='catalog')),
    path('user/', include('users.urls', namespace='user')),
    path('cart/', include('carts.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='order')),
    # Installs urls
    path('captcha/', include('captcha.urls')),
    # path('accounts/', include('allauth.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),  
    ]    
