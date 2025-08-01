from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # Handles login, logout, register, dashboard
    path('jobs/', include('jobs.urls')),  # job app
    path('', RedirectView.as_view(url='/login/', permanent=False)),  # Redirect root to login
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
