# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from django.conf.urls import url, include
from django.urls import path, include
from addresses import views
from django.contrib import admin

urlpatterns = [
    path('addresses/', views.address_list),
    path('addresses/<int:pk>/', views.address),
    path('login/', views.login),
    path('app_login/', views.app_login),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('chat_service/', views.chat_service),
]
