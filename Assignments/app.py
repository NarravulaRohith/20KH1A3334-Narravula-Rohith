from flask import Flask #importing library
app=Flask(__name__)#Creating the object
@app.route('/')#Decorator
def greeting_page():
    #linking from greeting_page to my_details
    return("<h1>Hello everyone.</h1><br><a href='http://127.0.0.1:5000/my_details'>My_details</a>")
@app.route('/my_details')
def my_details():
    return("<h3>Name:Narravula Rohith <br> Roll.No:20KH1A3334</h3>")
@app.route('/my_email_details')
def my_email_details():
    return("Email:2020csm.r34@svck.edu.in")

#creating simple home,login,registration pages with help of html tags
@app.route('/home')
def welcome():
    return("<body bgcolor='skyblue'><h1>Hello,this is home page</h1><br><a href='http://127.0.0.1:5000/login_page'><button>Login Page</button></a></body>")
@app.route('/login_page')
def login_page():
    return("<h2>Hello this is login page<h2><br><form>Email:<input type='text' name='email' id='email'><br>Password:<input type='text' name='pass' id='pass'><br><button>Submit</button><br></form><a href='http://127.0.0.1:5000/registration_page'><button>Registration_page</button></a>")
@app.route('/registration_page')
def registration_page():
    return("<h1>This is registraion page</h1><br><form>First Name:<input type='text'><br>Last Name:<input type='text'><br>Email:<input type='text'><br>Mobile.No:<input type='text'><br>Date of Birth:<input type='date'><br>Gender:<br><input type='radio' name='h1'>Male<br><input type='radio' name='h1'>Female<br><input type='checkbox'>Terms & Conditions<br><button>Submit</button></form>")

#creating a page to display fruits names
@app.route('/fruits_names')
def fruits_names():
    return('Apple,Mango,grapes,banana')

#creating a page displaying animals names
@app.route('/animal_names')
def animal_names():
    return("Elephant,Tiger,Dog,Sheep,Lion,Zebra,Cat,...etc")

#creating a page to display Mobile companies
@app.route('/mobile_companies')
def mobile_companies():
    return('iphone,Nokia,Redmi,Realme,Lenovo,asus,...etc.')

#creating a page to display Laptop companies
@app.route('/laptop_companies')
def laptop_companies():
    return('Macbook,Asus,HP,Lenovo,..etc')
    
if __name__=='__main__':
    app.run()