# 💰 Expense Tracker

A modern, full-stack web application for tracking personal income and expenses with beautiful visualizations and responsive design.

![Expense Tracker](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🔐 **User Authentication** - Secure registration and login system
- 💵 **Transaction Management** - Add, view, and delete income/expense transactions
- 📊 **Data Visualization** - Interactive charts showing monthly trends
- 📱 **Fully Responsive** - Works seamlessly on desktop, tablet, and mobile devices
- 🎨 **Modern UI** - Beautiful glass-morphism design with smooth animations
- 📈 **Dashboard Analytics** - Real-time income, expense, and balance tracking
- 🗑️ **Transaction History** - View all transactions with filtering options

## 🚀 Tech Stack

### Backend
- **Flask** - Python web framework
- **SQLAlchemy** - ORM for database management
- **Flask-Login** - User session management
- **Werkzeug** - Password hashing and security

### Frontend
- **HTML5** - Structure
- **Tailwind CSS** - Styling framework
- **JavaScript** - Interactive functionality
- **Chart.js** - Data visualization
- **Jinja2** - Template engine

### Database
- **SQLite** - Lightweight database (can be upgraded to PostgreSQL/MySQL)

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/cyb3erasad/Python-Expense-Tracker.git
cd expense-tracker
```

2. **Create a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create requirements.txt** (if not exists)
```txt
Flask==2.3.0
Flask-SQLAlchemy==3.0.3
Flask-Login==0.6.2
Werkzeug==2.3.0
```

5. **Set up environment variables**
```bash
# Windows
set FLASK_APP=app.py
set FLASK_ENV=development
set SECRET_KEY=your-secret-key-here

# macOS/Linux
export FLASK_APP=app.py
export FLASK_ENV=development
export SECRET_KEY=your-secret-key-here
```

6. **Initialize the database**
```bash
python
>>> from app import app, db
>>> with app.app_context():
>>>     db.create_all()
>>> exit()
```

7. **Run the application**
```bash
flask run
```

8. **Access the application**
Open your browser and navigate to: `http://localhost:5000`

## 📁 Project Structure

```
expense-tracker/
│
├── app.py                  # Main application file
├── models.py              # Database models
├── routes.py              # Route handlers
├── requirements.txt       # Python dependencies
│
├── templates/             # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── home.html         # Landing page
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   ├── dashboard.html    # Main dashboard with charts
│   ├── add_transaction.html  # Add transaction form
│   └── transactions.html # Transaction history
│
├── static/               # Static files (if needed)
│   ├── css/
│   ├── js/
│   └── images/
│
└── instance/             # Database file
    └── expense_tracker.db
```

## 🎯 Usage

### Register a New Account
1. Navigate to the homepage
2. Click "Register"
3. Fill in username, email, and password
4. Submit the form

### Login
1. Click "Login" from the homepage
2. Enter your email and password
3. Access your dashboard

### Add Transaction
1. Click "Add Transaction" from the navigation
2. Select transaction type (Income/Expense)
3. Enter amount, description, and date
4. Submit the form

### View Dashboard
- See your current month's income, expenses, and balance
- View monthly trends with interactive charts
- Analyze spending patterns

### Manage Transactions
- View all transactions in the History page
- Delete unwanted transactions
- Filter and search (coming soon)

## 🎨 Features in Detail

### Dashboard
- **Total Income** - Sum of all income transactions for current month
- **Total Expense** - Sum of all expense transactions for current month
- **Balance** - Difference between income and expenses
- **Monthly Bar Chart** - Compare income vs expenses across all months
- **Doughnut Chart** - Visual breakdown of income vs expenses

### Responsive Design
- **Mobile First** - Optimized for mobile devices
- **Card Layout** - Mobile-friendly transaction cards
- **Bottom Navigation** - Easy access on mobile
- **Touch Friendly** - Large buttons and touch targets

### Security Features
- Password hashing using Werkzeug
- User session management with Flask-Login
- CSRF protection
- Secure database queries with SQLAlchemy

## 📱 Mobile Features

- Bottom navigation bar for easy access
- Card-based transaction view
- Touch-optimized buttons
- Responsive charts
- Swipe gestures support (future)

## 🚧 Future Enhancements

- [ ] Export transactions to CSV/PDF
- [ ] Category-based expense tracking
- [ ] Budget setting and alerts
- [ ] Multi-currency support
- [ ] Recurring transactions
- [ ] Data backup and restore
- [ ] Advanced filtering and search
- [ ] Email notifications
- [ ] Dark mode toggle
- [ ] API for mobile app integration

## 🐛 Troubleshooting

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

ASAD NADEEM
- GitHub: [@cyb3erasad](https://github.com/cyb3erasad)
- Email: cyb3rasad@gmail.com

## 🙏 Acknowledgments

- Flask documentation
- Tailwind CSS for the styling framework
- Chart.js for beautiful charts
- The open-source community

---

Made with ❤️ and Python