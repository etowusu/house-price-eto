from flask import Flask, render_template, redirect, flash,url_for #render helps to load html files, after handling the form it is redirected to the form page. flash sends a flash message to the page after submission. 
from form import Prediction
from joblib import load
app  = Flask(__name__)  #initializing the app from flask. it will pick the name 'house price pred'

app.config['SECRET_KEY'] = '9359be8330ee3242b6667b165c427c7f' #this prevents csrf 
@app.route('/', methods=['GET', 'POST'])            # other examples '/about' '/contact'. to accept posts do the methods=post also
def home():                #set a definition fucntion on the home page '/' and tell it what it should do
    form = Prediction()     #calling the form.py class here onto the main page
    result = ''
    if form.validate_on_submit():  #if the user clicks submit/predict button
        data = [form.bedrooms.data,form.bathrooms.data,form.condition.data,form.floors.data,
            form.sqft_above.data,form.sqft_living.data,form.sqft_lot15.data,form.yr_built.data,
            form.zipcode.data, form.sqft_lot.data]  #the data inputted by the user will be stored as a list called data
    
        model = load('model.joblib')
        result = model.predict([data]) #the [] makes the dataframe a 2D array. adding another[] will make it 3D
        result = str(result).strip('[]')
        flash('The price is $'+ result)  #session ID can be used instead of flask to keep track of the user's session on the site
        return redirect(url_for('home')) #the whole of the if function is the post method
    return render_template('home.html', myform = form)  #form is assigned to a var and passed in the render templqtes 


if __name__ == '__main__':
    app.run(debug=True,port=33507)  #if name equals the main project then run the app. debug=true means show errors
                                     #the port is beacuse of heroku