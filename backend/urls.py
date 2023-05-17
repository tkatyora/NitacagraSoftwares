from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("main.urls")),
    path('learning/',include("learning.urls")),
    path('ourservices/',include("Ourservices.urls")),
    path('portal/',include("portal.urls")), 
    path('MurimiVangu/fowlrun/',include('MVAnimalManagement.urls'))  ,
    path('farmer/' , include('MVFarmers.urls'))     
]

urlpatterns += static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns = staticfiles_urlpatterns()
   
