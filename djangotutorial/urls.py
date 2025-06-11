from django.conf import settings
from django.urls import path, include

urlpatterns = [
    # ...existing code...
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]