from django.contrib import admin
from django.urls import path
import alcoholapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', alcoholapp.views.home, name="home"),
    path('new/', alcoholapp.views.new, name="new"),
    path('icecream/', alcoholapp.views.icecream, name="icecream"),
    path('beverage/', alcoholapp.views.beverage, name="beverage"),
    path('others/', alcoholapp.views.others, name="others"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
