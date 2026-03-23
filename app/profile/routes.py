from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.profile.forms import UpdateProfileForm
from app.extensions import db
from app.models.user import User
import os
from werkzeug.utils import secure_filename

profile_bp = Blueprint('profile', __name__, template_folder='templates/profile')

@profile_bp.route('/view', methods=['GET', 'POST'])
@login_required
def view_profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        current_user.fullname = form.fullname.data
        if form.avatar.data:
            filename = secure_filename(form.avatar.data.filename)
            avatar_path = os.path.join('app/static/img', filename)
            form.avatar.data.save(avatar_path)
            current_user.avatar = filename
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile.view_profile'))
    elif request.method == 'GET':
        form.fullname.data = current_user.fullname
    return render_template('view_profile.html', form=form, user=current_user)