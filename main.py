from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['POST', 'GET'])
def index():

    if request.method == 'GET':
        username = ''
        email = ''
        password = ''
        verify = ''

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        verify = request.form['verify']

        username_error = ''
        email_error = ''
        password_error = ''
        verify_error = ''

        if is_empty(verify):
            password_error = "Please re-enter your password"
            verify_error = "Please verify your password"
        if does_not_match(password, verify):
            password_error = "Please re-enter your password"
            verify_error = "Passwords must match"

        if is_out_of_range(username):
            username_error = "Usernames must be between 3-20 characters"
        if is_out_of_range(password):
            password_error = "Passwords must be between 3-20 characters"
            verify_error = ''

        if contains_space(username):
            username_error = "Usernames cannot contain spaces"
        if contains_space(password):
            password_error = "Passwords cannot contain spaces"

        if is_empty(username):
            username_error = "Please enter a username"
        if is_empty(password):
            password_error = "Please enter a password"

        if email:
            if is_not_email(email):
                email_error = "Please enter a valid email address"

        if username_error or email_error or password_error or verify_error:
            return render_template('index_homepage.html', title = "Signup",
                username = username, email = email,
                username_error = username_error,
                email_error = email_error,
                password_error = password_error,
                verify_error = verify_error)
        
        return render_template('welcome.html', title="Welcome, " + username,
                username=username)

    return render_template('index_homepage.html', title="Signup",
        username=username, email=email)

def is_empty(user_input):
    if user_input == '':
        return True
    else:
        return False

def is_out_of_range(user_input):
    if len(user_input) < 3 or len(user_input) > 20:
        return True
    else:
        return False

def contains_space(user_input):
    if ' ' in user_input:
        return True
    else:
        return False

def does_not_match(user_input, user_verify):
    if user_input != user_verify:
        return True
    else:
        return False

def is_not_email(user_input):
    dot = user_input.count('.')
    at = user_input.count('@')

    if dot != 1 or at != 1 or contains_space(user_input) or is_out_of_range(user_input):
        return True
    else:
        return False


app.run()