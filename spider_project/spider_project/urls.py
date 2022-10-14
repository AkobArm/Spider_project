from django.contrib import admin
from django.urls import path, include
from spider_market.views import RegistrationApiView, CategoriesView, CompaniesView, ProductView, ActiveProductsView,\
    CreateProductView, ModifyProductView, RegionView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('registr/', RegistrationApiView.as_view(), name='registr'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('companies/', CompaniesView.as_view(), name='companies'),
    path('product/<int:pk>', ProductView.as_view(), name='product'),
    path('activeproducts/', ActiveProductsView.as_view(), name='activeproducts'),
    path('createproduct/', CreateProductView.as_view(), name='createproduct'),
    path('modifyproduct/<int:pk>', ModifyProductView.as_view(), name='modifyproduct'),
]
