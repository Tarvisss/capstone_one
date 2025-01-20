from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField, SubmitField, SelectField, HiddenField
from wtforms.validators import DataRequired, Email, Length, Optional, URL, InputRequired


class PostForm(FlaskForm):
    """Form for adding/editing posts."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL', validators=[Optional(), URL()])
    type = HiddenField('User Type')

class UserUpdateForm(FlaskForm):
    """Form for updating users."""

    username = StringField('Username')
    email = StringField('E-mail', validators=[Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL')
    bio = StringField('(Optional) bio')
    header_image_url = StringField('(Optional) Header_Image URL')
    # before there wasn't a way to update the location
    location = StringField("(Optional) Where are you from? ")
    
class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class FanForm(FlaskForm):
    favorite_genre = StringField('Favorite Genre', validators=[DataRequired()])
    favorite_band = StringField('Favorite Band', validators=[DataRequired()])
    favorite_song = StringField('Favorite Song', validators=[DataRequired()])
    concert_ex = TextAreaField('Concert Experience')
    music_preference = TextAreaField('Music Preference')
    # submit = SubmitField('Save Fan Profile')

# Organizer-specific fields
class OrganizerForm(FlaskForm):
    organization_name = StringField('Name of your organization ', default=None, validators=[DataRequired()])
    event_description = TextAreaField('Types of events you host.',default=None, validators=[DataRequired()])
    venue_locations = StringField('Event Location.',default=None, validators=[DataRequired()])
    dates_unavailable = StringField('Dates the venue is not in operation''.',default=None, validators=[DataRequired()])
    venue_capacity = StringField('Our Venues capacity is.', default=None, validators=[DataRequired()])
    # submit = SubmitField('Save Organizer Profile')

# Musician-specific fields
class MusicianForm(FlaskForm):
    members = StringField('list memebers and their position in the band',default=None, validators=[DataRequired()])
    music_style = StringField('Musicial Style',default=None, validators=[DataRequired()])
    band_name = StringField('Band Name',default=None, validators=[DataRequired()])
    years_playing = StringField('Years Playing',default=None, validators=[DataRequired()])
    music_achievements = TextAreaField('Music Achievements', default="I'm a newbie",)
    # submit = SubmitField('Save Musician Profile')

class PreSignupForm(FlaskForm):
    choice = SelectField('', choices=[('1', 'Fan'), ('2', 'Organizer'), ('3', 'Musician')], validators=[InputRequired()])
    submit = SubmitField('Submit')