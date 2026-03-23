from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed

class UpdateProfileForm(FlaskForm):
    fullname = StringField('Full Name', validators=[DataRequired(), Length(max=50)])
    avatar = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update Profile')