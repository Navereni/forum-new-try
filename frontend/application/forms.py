from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField
from wtforms.validators import DataRequired

class CreatePostsForm(FlaskForm):
    name = StringField("Your Post", validators=[DataRequired()])
    datetime = DateTimeField("Date Posted")
    submit = SubmitField("Add Post")


class CreateCommentsForm(FlaskForm):
    name = StringField("Your Comment", validators=[DataRequired()])
    posts = SelectField("Posts", validators=[DataRequired()], choices=[])
    submit = SubmitField("Add Comment")