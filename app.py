from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from models import db, Office, Staff
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Home page with dashboard statistics"""
    total_offices = Office.query.count()
    total_staff = Staff.query.count()
    active_offices = Office.query.filter_by(status='Active').count()
    active_staff = Staff.query.filter_by(status='Active').count()
    
    recent_offices = Office.query.order_by(Office.created_at.desc()).limit(5).all()
    recent_staff = Staff.query.order_by(Staff.created_at.desc()).limit(5).all()
    
    return render_template('index.html', 
                         total_offices=total_offices,
                         total_staff=total_staff,
                         active_offices=active_offices,
                         active_staff=active_staff,
                         recent_offices=recent_offices,
                         recent_staff=recent_staff)

# Office Routes
@app.route('/offices')
def offices_list():
    """List all offices"""
    offices = Office.query.order_by(Office.name).all()
    return render_template('offices/list.html', offices=offices)

@app.route('/offices/<int:id>')
def office_detail(id):
    """View office details"""
    office = Office.query.get_or_404(id)
    return render_template('offices/detail.html', office=office)

@app.route('/offices/new', methods=['GET', 'POST'])
def office_new():
    """Create new office"""
    if request.method == 'POST':
        try:
            # Parse date
            established_date = None
            if request.form.get('established_date'):
                established_date = datetime.strptime(request.form['established_date'], '%Y-%m-%d').date()
            
            office = Office(
                name=request.form['name'],
                license_number=request.form['license_number'],
                location=request.form.get('location'),
                contact_person=request.form.get('contact_person'),
                phone=request.form.get('phone'),
                email=request.form.get('email'),
                established_date=established_date,
                status=request.form.get('status', 'Active'),
                description=request.form.get('description')
            )
            db.session.add(office)
            db.session.commit()
            flash('Office created successfully!', 'success')
            return redirect(url_for('office_detail', id=office.id))
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating office: {str(e)}', 'error')
    
    return render_template('offices/form.html', office=None)

@app.route('/offices/<int:id>/edit', methods=['GET', 'POST'])
def office_edit(id):
    """Edit office"""
    office = Office.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            office.name = request.form['name']
            office.license_number = request.form['license_number']
            office.location = request.form.get('location')
            office.contact_person = request.form.get('contact_person')
            office.phone = request.form.get('phone')
            office.email = request.form.get('email')
            
            if request.form.get('established_date'):
                office.established_date = datetime.strptime(request.form['established_date'], '%Y-%m-%d').date()
            
            office.status = request.form.get('status', 'Active')
            office.description = request.form.get('description')
            
            db.session.commit()
            flash('Office updated successfully!', 'success')
            return redirect(url_for('office_detail', id=office.id))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating office: {str(e)}', 'error')
    
    return render_template('offices/form.html', office=office)

@app.route('/offices/<int:id>/delete', methods=['POST'])
def office_delete(id):
    """Delete office"""
    office = Office.query.get_or_404(id)
    try:
        db.session.delete(office)
        db.session.commit()
        flash('Office deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting office: {str(e)}', 'error')
    
    return redirect(url_for('offices_list'))

# Staff Routes
@app.route('/staff')
def staff_list():
    """List all staff"""
    staff_members = Staff.query.order_by(Staff.full_name).all()
    return render_template('staff/list.html', staff_members=staff_members)

@app.route('/staff/<int:id>')
def staff_detail(id):
    """View staff details"""
    staff = Staff.query.get_or_404(id)
    return render_template('staff/detail.html', staff=staff)

@app.route('/staff/new', methods=['GET', 'POST'])
def staff_new():
    """Create new staff member"""
    offices = Office.query.order_by(Office.name).all()
    
    if request.method == 'POST':
        try:
            # Parse dates
            date_of_birth = None
            if request.form.get('date_of_birth'):
                date_of_birth = datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d').date()
            
            visa_expiry = None
            if request.form.get('visa_expiry'):
                visa_expiry = datetime.strptime(request.form['visa_expiry'], '%Y-%m-%d').date()
            
            contract_start = None
            if request.form.get('contract_start'):
                contract_start = datetime.strptime(request.form['contract_start'], '%Y-%m-%d').date()
            
            contract_end = None
            if request.form.get('contract_end'):
                contract_end = datetime.strptime(request.form['contract_end'], '%Y-%m-%d').date()
            
            salary = None
            if request.form.get('salary'):
                salary = float(request.form['salary'])
            
            staff = Staff(
                full_name=request.form['full_name'],
                nationality=request.form.get('nationality'),
                passport_number=request.form['passport_number'],
                position=request.form.get('position'),
                date_of_birth=date_of_birth,
                gender=request.form.get('gender'),
                phone=request.form.get('phone'),
                email=request.form.get('email'),
                visa_number=request.form.get('visa_number'),
                visa_expiry=visa_expiry,
                contract_start=contract_start,
                contract_end=contract_end,
                salary=salary,
                status=request.form.get('status', 'Active'),
                notes=request.form.get('notes'),
                office_id=request.form['office_id']
            )
            db.session.add(staff)
            db.session.commit()
            flash('Staff member created successfully!', 'success')
            return redirect(url_for('staff_detail', id=staff.id))
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating staff member: {str(e)}', 'error')
    
    return render_template('staff/form.html', staff=None, offices=offices)

@app.route('/staff/<int:id>/edit', methods=['GET', 'POST'])
def staff_edit(id):
    """Edit staff member"""
    staff = Staff.query.get_or_404(id)
    offices = Office.query.order_by(Office.name).all()
    
    if request.method == 'POST':
        try:
            staff.full_name = request.form['full_name']
            staff.nationality = request.form.get('nationality')
            staff.passport_number = request.form['passport_number']
            staff.position = request.form.get('position')
            
            if request.form.get('date_of_birth'):
                staff.date_of_birth = datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d').date()
            
            staff.gender = request.form.get('gender')
            staff.phone = request.form.get('phone')
            staff.email = request.form.get('email')
            staff.visa_number = request.form.get('visa_number')
            
            if request.form.get('visa_expiry'):
                staff.visa_expiry = datetime.strptime(request.form['visa_expiry'], '%Y-%m-%d').date()
            
            if request.form.get('contract_start'):
                staff.contract_start = datetime.strptime(request.form['contract_start'], '%Y-%m-%d').date()
            
            if request.form.get('contract_end'):
                staff.contract_end = datetime.strptime(request.form['contract_end'], '%Y-%m-%d').date()
            
            if request.form.get('salary'):
                staff.salary = float(request.form['salary'])
            
            staff.status = request.form.get('status', 'Active')
            staff.notes = request.form.get('notes')
            staff.office_id = request.form['office_id']
            
            db.session.commit()
            flash('Staff member updated successfully!', 'success')
            return redirect(url_for('staff_detail', id=staff.id))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating staff member: {str(e)}', 'error')
    
    return render_template('staff/form.html', staff=staff, offices=offices)

@app.route('/staff/<int:id>/delete', methods=['POST'])
def staff_delete(id):
    """Delete staff member"""
    staff = Staff.query.get_or_404(id)
    try:
        db.session.delete(staff)
        db.session.commit()
        flash('Staff member deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting staff member: {str(e)}', 'error')
    
    return redirect(url_for('staff_list'))

if __name__ == '__main__':
    app.run(debug=True)
