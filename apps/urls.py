from django.urls import path

from apps.views import ProductListView, delete_product, update_product,update_page

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('update', update_page, name='update_page'),
    path('delete-product/<int:pk>', delete_product, name='delete_product'),
    path('update-product', update_product, name='update_product'),
]
