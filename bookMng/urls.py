from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('postbook/', views.postbook, name='postbook'),
    path('displaybooks/', views.displaybooks, name='displaybooks'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('postreview/<int:book_id>', views.postreview, name='postreview'),
    path('searchbar/', views.searchbar, name='searchbar'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('placeorder', views.placeorder, name='placeorder'),
    
]
 