from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.artwork.forms import ArtworkForm
from app.models.artwork import Artwork
from app.extensions import db
import os
from werkzeug.utils import secure_filename

artwork_bp = Blueprint('artwork', __name__, template_folder='templates/artwork')

@artwork_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_artwork():
    form = ArtworkForm()
    if form.validate_on_submit():
        filename = None
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            image_path = os.path.join('app/static/img', filename)
            form.image.data.save(image_path)
        art = Artwork(
            title=form.title.data,
            description=form.description.data,
            price=form.price.data,
            image=filename,
            user_id=current_user.id
        )
        db.session.add(art)
        db.session.commit()
        flash('Artwork added successfully!', 'success')
        return redirect(url_for('artwork.gallery'))
    return render_template('add_artwork.html', form=form)

@artwork_bp.route('/gallery')
def gallery():
    artworks = Artwork.query.all()
    return render_template('gallery.html', artworks=artworks)

@artwork_bp.route('/<int:art_id>')
def artwork_detail(art_id):
    art = Artwork.query.get_or_404(art_id)
    return render_template('artwork_detail.html', art=art)