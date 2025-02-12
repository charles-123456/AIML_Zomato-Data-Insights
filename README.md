# Zomata - Food Delivery Data Insights Using Python and SQL

## Overview
This Streamlit application allows users to perform CRUD (Create, Read, Update, Delete) operations on an SQL database, dynamically modify table structures, and analyze key business insights using SQL queries and visualizations.

## Features
1. **Database Management:**
   - Add, update, and delete records from SQL tables.
   - Modify existing tables by adding new columns.
2. **Data Analysis & Insights:**
   - View peak ordering times.
   - Track delayed deliveries.
   - Analyze top customers based on order frequency and spending.
   - Evaluate restaurant popularity and performance.
   - Measure delivery personnel efficiency.
3. **Dynamic Table Loading:**
   - Select tables dynamically and display data in a structured format.
4. **Streamlit-based UI:**
   - User-friendly interface for database operations and insights visualization.

---

## Installation & Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- MySQL Database
- Virtual Environment (optional but recommended)

### Step 1: Clone the Repository
```sh
git clone https://github.com/your-repo/streamlit-db-insights.git
cd streamlit-db-insights
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 4: Configure Database Connection
Update the `config.py` file with your MySQL database credentials:
```python
DB_CONFIG = {
    "host": "your-database-host",
    "user": "your-username",
    "password": "your-password",
    "database": "your-database-name"
}
```

### Step 5: Run the Streamlit App
```sh
streamlit run app.py
```

---

## Usage

### 1. CRUD Operations
- **Add Record:** Enter table name, column names, and values to insert a new record.
- **Update Record:** Modify existing records by specifying conditions and new values.
- **Delete Record:** Remove unwanted records from tables.
- **Modify Table:** Add new columns to an existing table dynamically.

### 2. Data Analysis & Insights
- **Peak Ordering Times:** Identifies the busiest hours for orders.
- **Delayed Deliveries:** Highlights orders where actual delivery time exceeded the estimated time.
- **Top Customers:** Lists customers based on order count and total spending.
- **Popular Restaurants:** Displays the most frequently ordered restaurants.
- **Delivery Performance:** Analyzes delivery personnel efficiency using average delivery time.

### 3. Dynamic Table View
- Select a table from a dropdown to view its contents.
- Displays table data in an easy-to-read format.

---

## Troubleshooting
### Issue: `Authentication plugin 'caching_sha2_password' is not supported`
**Solution:** Run the following SQL command in MySQL:
```sql
ALTER USER 'your-username'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your-password';
FLUSH PRIVILEGES;
```

### Issue: `Data too long for column 'phone'`
**Solution:** Ensure the phone column is defined with a sufficient character limit:
```sql
ALTER TABLE Customers MODIFY COLUMN phone VARCHAR(20);
```

### Issue: `ModuleNotFoundError: No module named 'mysql.connector'`
**Solution:** Install MySQL Connector:
```sh
pip install mysql-connector-python
```

---

## Contributing
Feel free to contribute by submitting pull requests, reporting issues, or suggesting improvements!

---

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---

## Contact
For queries or support, reach out to:
- **Email:** charlesit333@example.com
- **GitHub:** [Your GitHub Profile](https://github.com/charles-123456)

