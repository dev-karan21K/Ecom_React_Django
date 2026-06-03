from django.urls import path
from users import views as UserViews
from products import views as ProductViews
from carts import views as CartViews
from orders import views as OrderViews

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserViews.RegisterView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('profile/', UserViews.ProfileView.as_view()),

    # categories api
    path('categories/', ProductViews.CategoryListView.as_view()),

    # products api
    path('products/', ProductViews.ProductListView.as_view()),
    path('products/<int:pk>/', ProductViews.ProductDetailView.as_view()),

    # cart api
    path('cart/', CartViews.CartListView.as_view()),
    path('cart/add/', CartViews.AddToCartView.as_view()),
    path('cart/items/<int:item_id>/', CartViews.ManageCartItemView.as_view()),

    # Orders
    path('orders/place/', OrderViews.PlaceOrderView.as_view()),
    path('orders/', OrderViews.MyOrdersView.as_view()),
    path('orders/<int:pk>/', OrderViews.OrderDetailView.as_view()),
]