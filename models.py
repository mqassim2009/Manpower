from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Office(db.Model):
    """Office/Company model for manpower agencies in Qatar"""
    __tablename__ = 'offices'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    license_number = db.Column(db.String(100), unique=True, nullable=False)
    location = db.Column(db.String(200))
    contact_person = db.Column(db.String(100))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(120))
    established_date = db.Column(db.Date)
    status = db.Column(db.String(50), default='Active')
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship with staff
    staff = db.relationship('Staff', backref='office', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Office {self.name}>'

class Staff(db.Model):
    """Staff/Employee model for manpower workers"""
    __tablename__ = 'staff'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(200), nullable=False)
    nationality = db.Column(db.String(100))
    passport_number = db.Column(db.String(50), unique=True, nullable=False)
    position = db.Column(db.String(100))
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(20))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(120))
    visa_number = db.Column(db.String(100))
    visa_expiry = db.Column(db.Date)
    contract_start = db.Column(db.Date)
    contract_end = db.Column(db.Date)
    salary = db.Column(db.Float)
    status = db.Column(db.String(50), default='Active')
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign key to Office
    office_id = db.Column(db.Integer, db.ForeignKey('offices.id'), nullable=False)
    
    def __repr__(self):
        return f'<Staff {self.full_name}>'
