from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.http import HttpResponse

def health(_):
    return HttpResponse("Project URLConf is active ✅")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health),                                # sanity check
    path("movies/", include("movies.urls")),                # app routes only here
    path("", RedirectView.as_view(pattern_name="movies:list", permanent=False)),
]
