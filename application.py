from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    pass
    # return "hi"

@app.route('/application')
def return_user_input():
    """Show resulting user input: firstname, lastname, salary request and job title."""

    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    salary = request.args.get("salary")
    position = request.args.get("position")

    return render_template("application-form.html",
                           firstname=firstname,
                           lastname=lastname,
                           salary=salary,
                           position=position,
                           )

# JINJA: 

# Thank you, {{ firstname }} {{ lastname }}, for applying to be a {{ position }}. Your
# minimum salary requirement is {{ salary }} dollars.

if __name__ == "__main__":
    app.run(debug=True)