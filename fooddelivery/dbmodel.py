from fooddelivery import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    contactno = db.Column(db.Numeric(10,0), unique=True)
    address_line1 = db.Column(db.String(50))
    address_line2 = db.Column(db.String(50))
    address_line3 = db.Column(db.String(50))
    pincode = db.Column(db.Integer)
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    country = db.Column(db.String(50))
    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"


class Category(db.Model):
    __tablename__="category"
    cid = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(100), nullable=False)

class Course(db.Model):
    __tablename__="course"
    coid = db.Column(db.Integer, primary_key=True)
    catgry_id = db.Column(db.Integer, db.ForeignKey(Category.__table__.c.cid), nullable=False)
    coname = db.Column(db.String(100), nullable=False)

class Restaurant(db.Model):
    __tablename__="restaurant"
    rid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contactno = db.Column(db.Numeric(10,0), unique=True)
    address_line1 = db.Column(db.String(50))
    address_line2 = db.Column(db.String(50))
    address_line3 = db.Column(db.String(50))
    pincode = db.Column(db.Integer)
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    country = db.Column(db.String(50))
    category_id = db.Column(db.String(50), db.ForeignKey(Category.__table__.c.cid), nullable=False)

    
class Product(db.Model):
    __tablename__="product"
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    details = db.Column(db.String(500), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(Category.__table__.c.cid), nullable=False)
    category_name = db.Column(db.String(50), db.ForeignKey(Category.__table__.c.cname), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey(Course.__table__.c.coid), nullable=False)
    course_name = db.Column(db.String(50), db.ForeignKey(Course.__table__.c.coname), nullable=False)
    rid = db.Column(db.Integer, db.ForeignKey(Restaurant.__table__.c.rid), nullable=False)
    image_file1 = db.Column(db.LargeBinary, nullable=False, default='default.jpg')
    quantity = db.Column(db.String(50), nullable=False)
    food_type = db.Column(db.String(10), nullable=False)
    iaa = db.Column(db.String(50), nullable=False)
    ibb = db.Column(db.String(50), nullable=False)
    icc = db.Column(db.String(50), nullable=False)
    idd = db.Column(db.String(50), nullable=False)
    iee = db.Column(db.String(50), nullable=False)
    iff = db.Column(db.String(50), nullable=False)
    

class Order(db.Model):
    __tablename__="order"
    oid = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey(User.__table__.c.id), nullable=False)
    pid = db.Column(db.Integer, db.ForeignKey(Product.__table__.c.pid), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    order_status = db.Column(db.String, nullable=False)

class UserTransac(db.Model):
    __tablename__="usertransac"
    transac_id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey(User.__table__.c.id), nullable=False)
    oid = db.Column(db.Integer, db.ForeignKey(Order.__table__.c.oid), nullable=False)
    upiid = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    transac_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    transac_details = db.Column(db.String(100))

class Shipping(db.Model):
    __tablename__="shipping"
    ship_id = db.Column(db.Integer, primary_key=True)
    oid = db.Column(db.Integer, db.ForeignKey(Order.__table__.c.oid), nullable=False)
    transac_id = db.Column(db.Integer, db.ForeignKey(UserTransac.__table__.c.transac_id), nullable=False)
    tracking_no = db.Column(db.Numeric(12,0), unique=True)#, nullable=False)
    delivery_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    details = db.Column(db.String(100))
    contactno = db.Column(db.Integer, unique=True, nullable=False)
    address_line1 = db.Column(db.String(50), nullable=False)
    address_line2 = db.Column(db.String(50))
    address_line3 = db.Column(db.String(50))
    pincode = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)


class Cart(db.Model):
    __tablename__="cart"
    uid = db.Column(db.Integer, db.ForeignKey(User.__table__.c.id), primary_key=True)
    pid = db.Column(db.Integer, db.ForeignKey(Product.__table__.c.pid), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

class Review(db.Model):
    __tablename__="review"
    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.__table__.c.id), primary_key=True, nullable=False)
    pid = db.Column(db.Integer, db.ForeignKey(Product.__table__.c.pid), primary_key=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.String(300), nullable=False)

