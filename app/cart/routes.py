from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.cart import CartItem
from app.models.artwork import Artwork
from app.extensions import db

cart_bp = Blueprint('cart', __name__, template_folder='templates/cart')

@cart_bp.route('/')
@login_required
def view_cart():
    items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.artwork.price * item.quantity for item in items)
    return render_template('view_cart.html', items=items, total=total)

@cart_bp.route('/add/<int:art_id>')
@login_required
def add_to_cart(art_id):
    existing = CartItem.query.filter_by(user_id=current_user.id, artwork_id=art_id).first()
    if existing:
        existing.quantity += 1
    else:
        item = CartItem(user_id=current_user.id, artwork_id=art_id, quantity=1)
        db.session.add(item)
    db.session.commit()
    flash('Artwork added to cart', 'success')
    return redirect(url_for('artwork.gallery'))

@cart_bp.route('/remove/<int:item_id>')
@login_required
def remove_from_cart(item_id):
    item = CartItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Item removed from cart', 'info')
    return redirect(url_for('cart.view_cart'))