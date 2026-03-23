from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, NumberRange

class ArtworkForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=500)])
    price = DecimalField('Price (USD)', validators=[DataRequired(), NumberRange(min=0)])
    image = FileField('Artwork Image', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add Artwork')