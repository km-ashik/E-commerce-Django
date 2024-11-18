from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib.sessions.models import Session

# Home Page
def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

# Product Detail
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/product_detail.html', {'product': product})

# Add to Cart
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)]['quantity'] += 1
    else:
        cart[str(id)] = {'quantity': 1}
    
    request.session['cart'] = cart
    return redirect('cart')

# Cart Page
from django.shortcuts import render
from .models import Product

def cart(request):
    # Retrieve the cart data from the session
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    # Debugging: Print the cart contents
    print("Session Cart Data:", cart)

    # Loop through each item in the cart
    for product_id, details in list(cart.items()):
        try:
            # Attempt to retrieve the product by ID
            product = Product.objects.get(id=product_id)
            quantity = details.get('quantity', 1)
            subtotal = product.price * quantity
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal
            })
            total_price += subtotal
        except Product.DoesNotExist:
            # Product no longer exists in the database, remove it from the session cart
            print(f"Product ID {product_id} not found. Removing from cart.")
            del cart[product_id]
            request.session['cart'] = cart  # Update session data

    # Debugging: Print the cart items after processing
    print("Cart Items to Display:", cart_items)

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })
Session.objects.all().delete()  # Clears all sessions

# Update Cart Quantity
def update_cart(request, id, action):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        if action == 'increment':
            cart[str(id)]['quantity'] += 1
        elif action == 'decrement':
            cart[str(id)]['quantity'] = max(1, cart[str(id)]['quantity'] - 1)
    
    request.session['cart'] = cart
    return redirect('cart')

# Remove from Cart
def remove_from_cart(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        del cart[str(id)]

    request.session['cart'] = cart
    return redirect('cart')

# Checkout Page
from django.shortcuts import render

def checkout(request):
    # Dummy Customer Details
    customer_address = {
        'name': 'John Doe',
        'address': 'House - 255 mini street',
        'city': 'malappuram',
        'state': 'Kerala',
        'pin': '676798',
    }
    return render(request, 'store/checkout.html', {'customer_address': customer_address})

# About Page
def about(request):
    return render(request, 'store/about.html')

# Contact Page
def contact(request):
    return render(request, 'store/contact.html')
