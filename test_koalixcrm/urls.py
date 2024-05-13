"""""from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]"""

from django.conf.urls.static import *
from django.contrib.staticfiles.urls import static
from django.contrib import admin
from filebrowser.sites import FileBrowserSite
from django.core.files.storage import DefaultStorage
from django.contrib import admin
from django.urls import path
from .views import landing_page_view


site = FileBrowserSite(name="filebrowser", storage=DefaultStorage())
customsite = FileBrowserSite(name='custom_filebrowser', storage=DefaultStorage())
customsite.directory = "uploads/"


admin.autodiscover()

urlpatterns = [
    path('admin/filebrowser/', customsite.urls),
    path('admin/', admin.site.urls),
    path('', landing_page_view, name='landing_page')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
