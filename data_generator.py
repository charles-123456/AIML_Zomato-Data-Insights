import random
from faker import Faker
import mysql.connector

# Initialize Faker
faker = Faker()

# Database connection
db = mysql.connector.connect(
    host="localhost",       # Change to your host
    user="charles",            # Your MySQL username
    password="charles@123",    # Your MySQL password
    database="zemato"  # Your database name
)
cursor = db.cursor()

# Insert fake data
def insert_fake_data():
    # Number of records to create
    num_customers = 50
    num_restaurants = 20
    num_orders = 100
    num_delivery_persons = 15

    # Insert Customers
    customer_ids = []
    for _ in range(num_customers):
        name = faker.name()
        email = faker.unique.email()
        phone = faker.phone_number()
        location = faker.address()
        signup_date = faker.date_this_year()
        is_premium = random.choice([True, False])
        preferred_cuisine = random.choice(['Indian', 'Chinese', 'Italian', 'Mexican'])
        total_orders = random.randint(0, 20)
        average_rating = round(random.uniform(1, 5), 2)
        
        cursor.execute("""
            INSERT INTO Customers (name, email, phone, location, signup_date, is_premium, preferred_cuisine, total_orders, average_rating)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (name, email, phone, location, signup_date, is_premium, preferred_cuisine, total_orders, average_rating))
        db.commit()
        customer_ids.append(cursor.lastrowid)

    # Insert Restaurants
    restaurant_ids = []
    for _ in range(num_restaurants):
        name = faker.company()
        cuisine_type = random.choice(['Indian', 'Chinese', 'Italian', 'Mexican'])
        location = faker.city()
        owner_name = faker.name()
        avg_delivery_time = random.randint(10, 60)
        contact_number = faker.phone_number()
        rating = round(random.uniform(1, 5), 2)
        total_orders = random.randint(0, 100)
        is_active = random.choice([True, False])
        
        cursor.execute("""
            INSERT INTO Restaurants (name, cuisine_type, location, owner_name, average_delivery_time, contact_number, rating, total_orders, is_active)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (name, cuisine_type, location, owner_name, avg_delivery_time, contact_number, rating, total_orders, is_active))
        db.commit()
        restaurant_ids.append(cursor.lastrowid)

    # Insert Orders
    order_ids = []
    for _ in range(num_orders):
        customer_id = random.choice(customer_ids)
        restaurant_id = random.choice(restaurant_ids)
        order_date = faker.date_time_this_year()
        delivery_time = faker.date_time_this_year() if random.random() > 0.2 else None
        status = random.choice(['Pending', 'Delivered', 'Cancelled'])
        total_amount = round(random.uniform(10, 100), 2)
        payment_mode = random.choice(['Credit Card', 'Cash', 'UPI'])
        discount_applied = round(random.uniform(0, 20), 2)
        feedback_rating = round(random.uniform(1, 5), 1) if status == 'Delivered' else None
        
        cursor.execute("""
            INSERT INTO Orders (customer_id, restaurant_id, order_date, delivery_time, status, total_amount, payment_mode, discount_applied, feedback_rating)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (customer_id, restaurant_id, order_date, delivery_time, status, total_amount, payment_mode, discount_applied, feedback_rating))
        db.commit()
        order_ids.append(cursor.lastrowid)

    # Insert Delivery Persons
    delivery_person_ids = []
    for _ in range(num_delivery_persons):
        name = faker.name()
        contact_number = faker.phone_number()
        vehicle_type = random.choice(['Bike', 'Car'])
        total_deliveries = random.randint(0, 100)
        avg_rating = round(random.uniform(1, 5), 2)
        location = faker.city()
        
        cursor.execute("""
            INSERT INTO DeliveryPersons (name, contact_number, vehicle_type, total_deliveries, average_rating, location)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, contact_number, vehicle_type, total_deliveries, avg_rating, location))
        db.commit()
        delivery_person_ids.append(cursor.lastrowid)

    # Insert Deliveries
    for order_id in order_ids:
        if random.random() > 0.3:  # 70% of orders have deliveries
            delivery_person_id = random.choice(delivery_person_ids)
            delivery_status = random.choice(['On the way', 'Delivered'])
            distance = round(random.uniform(0.5, 20), 2)
            delivery_time = random.randint(10, 60) if delivery_status == 'Delivered' else None
            estimated_time = random.randint(10, 60)
            delivery_fee = round(random.uniform(5, 15), 2)
            vehicle_type = random.choice(['Bike', 'Car'])
            
            cursor.execute("""
                INSERT INTO Deliveries (order_id, delivery_person_id, delivery_status, distance, delivery_time, estimated_time, delivery_fee, vehicle_type)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (order_id, delivery_person_id, delivery_status, distance, delivery_time, estimated_time, delivery_fee, vehicle_type))
            db.commit()

# Run the function
insert_fake_data()

# Close the connection
cursor.close()
db.close()
