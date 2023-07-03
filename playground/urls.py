from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html")),
    path("add-product-form/", TemplateView.as_view(template_name="add_product.html")),
    path("delete-product-form/", views.show_delete_form),
    path("update-product-form", views.show_update_form),
    path("show-product-form", views.show_product_form),
    path("show-product/", views.show_product),
    path("show-product/<str:name>",views.show_product),
    path("show-products", views.show_products),
    path("remove-product", views.remove_product),
    path("create-product", views.insert_product),
    path("update-product", views.update_product),
]
