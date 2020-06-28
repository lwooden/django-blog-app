
from django.contrib import admin
from django.urls import path, include


# Bring in the urls from the "blog" app in the main URL patterns of the project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog'))
]
