from . import views
from django.urls import include, path

urlpatterns = [
    path('budget_extension/',views.extension_view),
]