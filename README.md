"# Qatar Manpower Management System

A comprehensive web-based manpower management system built with Python Flask for managing office profiles and staff members in Qatar. This system provides powerful features to control and track office details, staff profiles, contracts, visas, and more.

## Features

### Office Management
- Create, read, update, and delete office profiles
- Track office license numbers and establishment dates
- Manage office contact information and locations
- Monitor office status (Active/Inactive/Suspended)
- View all staff members associated with each office

### Staff Management
- Complete staff profile management (CRUD operations)
- Personal information tracking (name, nationality, date of birth, gender)
- Employment details (position, salary, contract dates)
- Passport and visa information management
- Visa expiry tracking and alerts
- Status monitoring (Active/On Leave/Terminated/Resigned)
- Notes and additional information storage

### Dashboard
- Quick overview of total offices and staff
- Active offices and staff count
- Recent additions to offices and staff
- Easy navigation to all sections

### User Interface
- Modern, responsive design using Bootstrap 5
- Intuitive navigation and user-friendly forms
- Mobile-friendly interface
- Color-coded status badges
- Interactive data tables
- Confirmation dialogs for delete operations

## Technology Stack

- **Backend**: Python 3.x with Flask
- **Database**: SQLite (can be easily configured for PostgreSQL/MySQL)
- **ORM**: Flask-SQLAlchemy
- **Frontend**: HTML5, Bootstrap 5, Bootstrap Icons
- **CSS**: Custom styling with responsive design

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/mqassim2009/Manpower.git
cd Manpower
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

## Usage

### Adding an Office
1. Navigate to "Offices" in the navigation menu
2. Click "Add New Office" button
3. Fill in the office details (name, license number, location, contact info, etc.)
4. Click "Create Office" to save

### Adding Staff Members
1. Ensure at least one office is created
2. Navigate to "Staff" in the navigation menu
3. Click "Add New Staff" button
4. Fill in staff details including personal info, employment details, and visa information
5. Select the office from the dropdown
6. Click "Create Staff Member" to save

### Viewing Details
- Click on any office or staff member name to view detailed information
- Use the "Edit" button to modify information
- Use the "Delete" button to remove records (with confirmation)

### Dashboard Overview
- The home page displays statistics and recent additions
- Quickly access recent offices and staff members
- Monitor active vs. total counts

## Database Schema

### Office Table
- id (Primary Key)
- name
- license_number (Unique)
- location
- contact_person
- phone
- email
- established_date
- status
- description
- created_at
- updated_at

### Staff Table
- id (Primary Key)
- full_name
- nationality
- passport_number (Unique)
- position
- date_of_birth
- gender
- phone
- email
- visa_number
- visa_expiry
- contract_start
- contract_end
- salary
- status
- notes
- office_id (Foreign Key to Office)
- created_at
- updated_at

## Configuration

You can configure the application by modifying `config.py`:

- **SECRET_KEY**: Change this in production for security
- **SQLALCHEMY_DATABASE_URI**: Configure database connection (default: SQLite)

For production deployment, set environment variables:
```bash
export SECRET_KEY='your-secret-key-here'
export DATABASE_URL='your-database-url-here'
```

## Project Structure

```
Manpower/
├── app.py                  # Main application file
├── models.py              # Database models
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Dashboard
│   ├── offices/          # Office templates
│   │   ├── list.html
│   │   ├── detail.html
│   │   └── form.html
│   └── staff/            # Staff templates
│       ├── list.html
│       ├── detail.html
│       └── form.html
└── static/               # Static files
    └── css/
        └── style.css     # Custom styles
```

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Security Considerations

- Always change the SECRET_KEY in production
- Use environment variables for sensitive configuration
- Implement proper authentication and authorization if deploying publicly
- Use HTTPS in production
- Regular backups of the database are recommended

## Future Enhancements

Potential features for future versions:
- User authentication and role-based access control
- Document upload and management
- Advanced search and filtering
- Export to PDF/Excel functionality
- Email notifications for visa expiry
- Multi-language support (Arabic/English)
- Reporting and analytics dashboard
- API endpoints for integration

## License

This project is open source and available for use and modification.

## Support

For issues, questions, or contributions, please open an issue on GitHub.

## Author

Qatar Manpower Management System - Developed for efficient manpower management in Qatar." 
