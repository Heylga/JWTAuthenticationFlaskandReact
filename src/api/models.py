from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


    def login_user(email, password):
        user = User.query.filter_by(email=email, password=password).first()
        return user
    
    def login_user(email, password):
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()

   #this function will save the new user in the database
    def save_user(email, password):
        


        #lets save the user in the database
        db.session.add(user)
        db.session.commit()