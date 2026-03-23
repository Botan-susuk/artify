from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.cart import CartItem
from app.models.order import Order, OrderItem
from app.extensions import db
from app.order.forms import CheckoutForm

order_bp = Blueprint('order', __name__, template_folder='templates/order')

@order_bp.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    form = CheckoutForm()
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    if not cart_items:
        flash('Your cart is empty.', 'warning')
        return redirect(url_for('cart.view_cart'))

    total = sum(item.artwork.price * item.quantity for item in cart_items)

    if form.validate_on_submit():
        order = Order(user_id=current_user.id)
        db.session.add(order)
        db.session.commit() 

        for item in cart_items:
            order_item = OrderItem(
                order_id=order.id,
                artwork_id=item.artwork.id,
                quantity=item.quantity
            )
            db.session.add(order_item)
            db.session.delete(item)
        db.session.commit()
        flash('Order placed successfully!', 'success')
        return redirect(url_for('order.order_history'))

    return render_template('checkout.html', form=form, items=cart_items, total=total)

@order_bp.route('/history')
@login_required
def order_history():
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return render_template('order_history.html', orders=orders)