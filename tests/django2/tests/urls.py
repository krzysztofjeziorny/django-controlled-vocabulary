from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    # PATCH
    path("vocabularies/", include("controlled_vocabulary.urls")),
]
