from flask_wtf import Form
from wtforms import TextAreaField, StringField, SubmitField, FileField, ValidationError
from wtforms.validators import DataRequired, Length
from app.models import Store


class StoreForm(Form):
    """
    Create a store form structure
    """
    store_name = StringField("Name: ", validators=[DataRequired("Please enter the store name."), Length(min=3, max=70, message="Store name should be more than 3 characters long and less than 70")])
    store_desc = TextAreaField("Description: ", validators=[Length(min=1, message="Description is too short")])
    store_img = FileField("Store Image: ")
    submit = SubmitField("Create Store")
