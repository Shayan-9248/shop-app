from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from .sitemap import ProductSitemap
from . import views

app_name = 'product'


sitemaps = {
    'static': ProductSitemap,
}


urlpatterns = [
    path('products/', views.ProductList.as_view(), name='list'),
    path('category/<slug:slug>/', views.ProductList.as_view(), name='category'),
    path('product/<slug:slug>/<int:id>/', views.product_detail, name='detail'),
    path('add-comment/<int:id>/', views.add_comment, name='comment'),
    path('add-reply/<int:id>/<int:comment_id>/', views.add_reply, name='reply'),
    path('add-to-favourite/<int:id>/', views.add_favourite, name='fav'),
    path('favourite-list/', views.favourite_list, name='fav-list'),
    path('api/comments/', include('shop_product.api.urls', namespace='api-comment')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]