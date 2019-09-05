from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, SubmitField  #drop down field, date field, etc can all be found in wtf 
from wtforms.validators import DataRequired   #DataRequired shows the input that is required to make (that is not an optional tab) 

class Prediction(FlaskForm):                    #class then name of the form, then the inheritance. the class will inherit the flask form functionalities
    bedrooms = IntegerField('Number of Bedrooms', validators =[DataRequired()])            #the fields that the users will be making input in and the type of inputs that will be made. with msg to display in the tab
    bathrooms = IntegerField('Number of Bathrooms', validators=[DataRequired()])
    sqft_living = DecimalField('Sqft living', validators=[DataRequired()])
    floors = IntegerField('Floors', validators=[DataRequired()])
    sqft_above = DecimalField('Sqft above', validators=[DataRequired()])
    sqft_lot = DecimalField('Sqft_Lot', validators=[DataRequired()])
    sqft_lot15 = DecimalField('Sqft_Lot15', validators=[DataRequired()])
    yr_built = IntegerField('Year Built', validators=[DataRequired()])
    condition = IntegerField('Condition', validators=[DataRequired()])
    zipcode = IntegerField('Zipcode', validators=[DataRequired()])
    submit = SubmitField('Predict')