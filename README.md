
# Monevance

**Monevance** is a personal finance management application built with Django. It allows users to effortlessly track their incomes and expenses, categorize financial transactions, and generate insightful reports to manage their finances effectively.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **User Authentication:** Secure registration and login system.
- **Category Management:** Create, view, update, and delete financial categories.
- **Income & Expense Tracking:** Add, view, and manage incomes and expenses linked to categories.
- **Report Generation:** Download reports of financial transactions.
- **Responsive Design:** User-friendly interface optimized for both desktop and mobile devices.

## Technologies Used

- **Backend:** Django 4.x
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite (default for Django)
- **Version Control:** Git

## Installation

Follow these steps to set up Monevance locally:

1. **Clone the Repository**
    ```bash
    git clone https://github.com/MuratGaytemirovv/monevance.git
    ```

2. **Navigate to the Project Directory**
    ```bash
    cd monevance
    ```

3. **Create a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. **Install Dependencies**
    ```bash
    pip install Django
    # Install other dependencies as needed, e.g., pip install djangorestframework
    ```
    
    *It's recommended to generate a `requirements.txt` for consistency:*
    ```bash
    pip freeze > requirements.txt
    ```

5. **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

6. **Create a Superuser (Optional)**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

8. **Access the Application**
    Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage

1. **Register or Log In:** Create a new account or log in with your existing credentials.
2. **Manage Categories:** Navigate to the "Add Category" section to create financial categories.
3. **Track Incomes and Expenses:** Use the respective sections to add, view, update, or delete your financial transactions.
4. **Download Reports:** Generate and download reports of your financial activities.
5. **Admin Panel:** Access the Django admin panel at `http://127.0.0.1:8000/admin/` to manage users and data directly.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**
2. **Create a New Branch**
    ```bash
    git checkout -b feature/YourFeatureName
    ```
3. **Commit Your Changes**
    ```bash
    git commit -m "Add your feature"
    ```
4. **Push to the Branch**
    ```bash
    git push origin feature/YourFeatureName
    ```
5. **Open a Pull Request**

## Contact

- **Email:** murat.gaytemirov@example.com
- **GitHub:** [MuratGaytemirovv](https://github.com/MuratGaytemirovv)



 
