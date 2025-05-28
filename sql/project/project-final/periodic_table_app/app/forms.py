from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange, Optional, Length, ValidationError
from app.models import Element

def unique_atomic_number(form, field):
    existing_element = None
    if hasattr(form, 'obj') and form.obj:
        if form.obj.atomic_number != field.data:
            existing_element = Element.query.filter_by(atomic_number=field.data).first()
    else:
        existing_element = Element.query.filter_by(atomic_number=field.data).first()
    
    if existing_element:
        raise ValidationError(f'Atomic number {field.data} already exists.')

def unique_symbol(form, field):
    existing_element = None
    if hasattr(form, 'obj') and form.obj:
        if form.obj.symbol.lower() != field.data.lower():
            existing_element = Element.query.filter(Element.symbol.ilike(field.data)).first()
    else:
        existing_element = Element.query.filter(Element.symbol.ilike(field.data)).first()

    if existing_element:
        raise ValidationError(f'Symbol "{field.data}" already exists.')

class ElementForm(FlaskForm):
    atomic_number = IntegerField('Atomic Number', validators=[DataRequired(), NumberRange(min=1, max=300), unique_atomic_number])
    symbol = StringField('Symbol', validators=[DataRequired(), Length(min=1, max=10), unique_symbol])
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=50)])
    atomic_mass = FloatField('Atomic Mass', validators=[DataRequired(), NumberRange(min=0.1)])
    group = IntegerField('Group', validators=[Optional(), NumberRange(min=1, max=18)])
    period = IntegerField('Period', validators=[Optional(), NumberRange(min=1, max=10)])
    element_type = SelectField('Element Type', validators=[Optional()], choices=[('', 'Select Type (Optional)')])
    description = TextAreaField('Description', validators=[Optional()])
    phase_choices = [('', 'Select Phase (Optional)'), ('Solid', 'Solid'), ('Liquid', 'Liquid'), ('Gas', 'Gas'), ('Unknown', 'Unknown')]
    phase = SelectField('Phase', choices=phase_choices, validators=[Optional()])
    
    appearance = StringField('Appearance', validators=[Optional(), Length(max=255)])
    density = FloatField('Density (g/cm³)', validators=[Optional(), NumberRange(min=0)])
    melt = FloatField('Melting Point (K)', validators=[Optional()])
    boil = FloatField('Boiling Point (K)', validators=[Optional()])
    discovered_by = StringField('Discovered By', validators=[Optional(), Length(max=255)])
    molar_heat = FloatField('Molar Heat (J/(mol·K))', validators=[Optional(), NumberRange(min=0)])
    named_by = StringField('Named By', validators=[Optional(), Length(max=255)])
    source = StringField('Source URL (e.g., Wikipedia)', validators=[Optional(), Length(max=500)])

    submit = SubmitField('Submit Element') 