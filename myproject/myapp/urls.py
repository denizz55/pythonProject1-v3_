from django.urls import path
from . import views
from .views import CreateProduct, UpdateProduct, DeleteProduct

urlpatterns = [
    path('', views.index, name='home'),
    path('products', views.ProductList.as_view(), name='products'),
    path('createproduct/', CreateProduct.as_view(), name='createproduct'),
    path('updateproduct/<int:pk>/', UpdateProduct.as_view(), name='updateproduct'),
    path('deleteproduct/<int:pk>/', DeleteProduct.as_view(), name='deleteproduct'),
    path('register', views.RegisterList.as_view(), name='register'),
    path('createregister/', views.CreateRegister.as_view(), name='createregister'),
    path('createregistersale/', views.CreateRegisterSale.as_view(), name='createregistersale'),
    path('percent/', views.PercentList.as_view(), name='percent'),
    path('percentcreate/', views.PercentCreate.as_view(), name='percentcreate'),
    path('profit/', views.Profit, name='profit'),
    path('profit_by_mounth/', views.profit_by_mounth, name='profit_by_mounth'),
]
