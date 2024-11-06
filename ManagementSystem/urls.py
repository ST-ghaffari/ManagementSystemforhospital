from django.contrib import admin
from django.urls import path, include
# ********* STGH **************
from django.conf import settings #add this
from django.conf.urls.static import static #add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('',include('doctor.urls')),
    path('',include('patient.urls')),
    path('',include('hospital.urls')),
    path('',include('userSystem.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

