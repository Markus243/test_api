from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# create the object of Flask
app = Flask(__name__)

# SqlAlchemy Database Configuration With Mysql


db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String(120), unique=True)
    klientid = db.Column(db.String(120), unique=True)

    def __init__(self, datetime, klientid):
        self.datetime = datetime
        self.klientid = klientid


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('datetime', 'klientid')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


# creating our routes
@app.route('/home', methods=['POST'])
def index():
    datetime = request.json['datetime']
    klientid = request.json['klientid']

    new_user = User(datetime, klientid)

    db.session.add(new_user)
    db.session.commit()

    return 'completed'


# run flask app
if __name__ == "__main__":
    app.run(debug=True)
