#We will create our Flask app in flask-app.py. Within flask-app.py we need to import the Flask package,
# which we do with this line of code.

from flask import Flask

#The above line of code basically means import the class Flask from the python package called flask.

#The next thing we need to do is create an
#instance of the Flask class. We will call this instance 'app' with the following line of code:

app = Flask(__name__)

#Now 'app' is our Flask object. Using 'app' we can define routes for our web application.
#A route defines what URLs our web application will respond to.
#For instance if can create a route /hello then our web application will do something
#when URL localhost:5000/hello is hit. Let's create the /hello route with the following line of code:

@app.route('/hello')


#To define what our web application does when that route is hit we need to define a function
# immediately below that route. Let's define a function called hello that returns the string
# 'Hello World!':

def hello():
    return 'Hello World!'

# now create another route

@app.route('/hi')

# now define what the 'hi' route will do
def hi():
    return 'Greetings old chum!'

#All that is left to do is to run the app, which we do by adding the following line of code:

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

#The if statement makes sure the application only runs if the script is executed directly from
#the Python interpreter and not used as an imported module.
#The app.run actually runs the application.

#To start our application we go to our terminal and execute the following command:

#  python3 flask-app.py

#If successful you should see the following output in the terminal:

#  * Running on http://127.0.0.1:5000/
# * Restarting with reloader
#Now if we go to a browser and enter URL http://localhost:5000/hello,
# it should come back with 'Hello World!'.
