from flask import Flask, render_template, redirect, request, flash, session
from model import connect_to_db, User, db

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "SECRET"

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

################################################################################

@app.route("/")
def homepage():
    """Shows homepage."""

    return render_template("index.html")

@app.route("/", methods=["POST"])
def add_user_questions():
    """Creates a new trip."""

    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    email = request.form.get("email")
    phonenumber = request.form.get("phonenumber")
    question = request.form.get("questions")

    user_question = User(email=email,
                        firstname=firstname,
                        lastname=lastname,
                        phonenumber=phonenumber,
                        question=question)
    
    db.session.add(user_question)
    db.session.commit()

    twilio(email)

    return redirect("/")


def twilio(email):
    user = User.query.get(email)
    cell_phone_number = user.phonenumber
    print cell_phone_number
    body = "Hello "+(user.firstname)+", thank you for sending us your questions, we will get back to you with a response as soon as we can."

    account_sid = "ACa5d79f5e8def42ccd889d962fac11b09"
    auth_token = "f57cb3a64e3ba882518a20ed3b0f0f59"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(to=cell_phone_number, from_="+14243221288",
                                    body=body)
    flash("Your message was sent successfully.")
    return redirect("/")


################################################################################

if __name__ == "__main__":

    connect_to_db(app)

    app.run(debug=True, host='0.0.0.0')
