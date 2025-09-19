from django.urls import path
from django.conf import settings
from . import views

# URL patterns specific to the hw app:
urlpatterns = [
    # path(r"", views.main_page, name="main_page"),
    path(r"main", views.main_page, name="main_page"),
    path(r"order", views.order_page, name="order_page"),
    path(r"confirmation", views.confirmation_page, name="confirmation_page"),
    # path(r"confirmation", views.show_all_page, name="show_all_page"),
]
