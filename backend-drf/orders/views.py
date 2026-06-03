from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from carts.models import Cart
from rest_framework.response import Response
from orders.models import Order, OrderedItem
from .serializers import OrderSeriailizer, OrderedItemSeriailizer
from rest_framework import status
from .utils import send_order_notification
from rest_framework.generics import ListAPIView, RetrieveAPIView

# Create your views here.
class PlaceOrderView(APIView):
    # check if the user is logged in
    permission_classes = [IsAuthenticated]

    # check if the cart is empty
    def post(self, request):
        cart = Cart.objects.get(user=request.user)
        print('cart==>', cart)
        # shipping_address = request.data.get('shippingAddress')
        if not cart or cart.items.count() == 0:
            return Response({"error": "Cart is empty"})
   
        # create the order
        order = Order.objects.create(
            user = request.user,
            subtotal = cart.subtotal,
            tax_amount = cart.tax_amount,
            grand_total = cart.grand_total,
            status = 'CONFIRMED',
            # address = shipping_address.get('address'),
            # phone = shipping_address.get('phone'),
            # city = shipping_address.get('city'),
            # state = shipping_address.get('state'),
            # zip_code = shipping_address.get('zip_code')
        )

        # create the order items
        for item in cart.items.all():
            OrderedItem.objects.create(
                order = order,
                product = item.product,
                quantity = item.quantity,
                price = item.product.price,
                total_price = item.total_price,
            )
        # clear the cart
        # cart.items.all().delete() automatically delete
        cart.delete()
        cart.save()

        # send a notification email
        send_order_notification(order)

        # send the response to frontend
        serializer = OrderSeriailizer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class MyOrdersView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSeriailizer
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSeriailizer

    def get_object(self):
        pk = self.kwargs.get('pk')
        order = get_object_or_404(Order, pk=pk, user=self.request.user)
        return order