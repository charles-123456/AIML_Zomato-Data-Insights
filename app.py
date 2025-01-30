import streamlit as st
import pandas as pd
from models import DatabaseOperations
from utils import (
    plot_peak_times
)

# Create an instance of DatabaseOperations class
db_ops = DatabaseOperations()

# Sidebar for navigation
st.sidebar.title("Database Operations")
selection = st.sidebar.radio("Choose an operation", ("CRUD Operations", "Data Analysis", "Insights"))

# CRUD Operations Menu
if selection == "CRUD Operations":
    crud_selection = st.selectbox("Select Operation", ["Add", "Update", "Delete", "Modify Table"])

    # Adding a new record
    if crud_selection == "Add":
        st.title("Add New Record")
        table_name = st.text_input("Table Name")
        column_names = st.text_area("Column Names (comma separated)").split(",")
        column_values = st.text_area("Column Values (comma separated)").split(",")
        
        if st.button("Add Record"):
            db_ops.add_record(table_name, column_names, column_values)

    # Updating an existing record
    elif crud_selection == "Update":
        st.title("Update Existing Record")
        table_name = st.text_input("Table Name")
        condition = st.text_input("Condition (e.g., customer_id=1)")
        column_names = st.text_area("Column Names (comma separated)").split(",")
        column_values = st.text_area("Column Values (comma separated)").split(",")
        
        if st.button("Update Record"):
            db_ops.update_record(table_name, column_names, column_values, condition)

    # Deleting a record
    elif crud_selection == "Delete":
        st.title("Delete Record")
        table_name = st.text_input("Table Name")
        condition = st.text_input("Condition (e.g., customer_id=1)")
        
        if st.button("Delete Record"):
            db_ops.delete_record(table_name, condition)

    # Modify Table Structure
    elif crud_selection == "Modify Table":
        st.title("Modify Table Structure")
        table_name = st.text_input("Table Name")
        new_column_name = st.text_input("New Column Name")
        column_type = st.text_input("Column Type (e.g., INT, VARCHAR)")
        
        if st.button("Add Column"):
            db_ops.add_column(table_name, new_column_name, column_type)

# Data Analysis Menu (Dynamic Table Loading)
elif selection == "Data Analysis":
    st.title("Data Analysis")
    
    # Fetch available tables in the database
    tables_query = "SHOW TABLES"
    tables_df = db_ops.fetch_as_dataframe(tables_query)
    if not tables_df.empty:
        table_names = tables_df.iloc[:, 0].tolist()
        selected_table = st.selectbox("Select a Table for Analysis", table_names)

        # Fetch and display selected table data
        if selected_table:
            st.write(f"Displaying data from {selected_table} table")
            table_query = f"SELECT * FROM {selected_table}"
            table_data = db_ops.fetch_as_dataframe(table_query)
            st.dataframe(table_data)
    else:
        st.error("No tables found in the database.")

# Insights Menu
elif selection == "Insights":
    insight_selection = st.selectbox("Select Insight", ["Peak Times", "Delayed Deliveries", "Top Customers", "Popular Restaurants", "Delivery Performance"])

    # Peak Times Insight
    if insight_selection == "Peak Times":
        order_query = """
        SELECT HOUR(order_date) AS hour, COUNT(*) AS order_count
        FROM Orders
        GROUP BY HOUR(order_date)
        ORDER BY order_count DESC
        """
        df = db_ops.fetch_as_dataframe(query=order_query)
        if not df.empty:
            plot_peak_times(df)
        else:
            st.error("No data available for Peak Times")

    # Delayed Deliveries Insight
    elif insight_selection == "Delayed Deliveries":
        delivery_query = """
        SELECT * FROM Deliveries
        WHERE delivery_time > estimated_time
        """
        df = db_ops.fetch_as_dataframe(query=delivery_query)
        if not df.empty:
            st.write(df)
        else:
            st.error("No delayed deliveries found.")

    # Top Customers Insight
    elif insight_selection == "Top Customers":
        top_customer_query = """
        SELECT customer_id, COUNT(order_id) AS order_count, SUM(total_amount) AS total_spent
        FROM Orders
        GROUP BY customer_id
        ORDER BY order_count DESC
        LIMIT 10
        """
        df = db_ops.fetch_as_dataframe(query=top_customer_query)
        if not df.empty:
            st.write(df)
        else:
            st.error("No data available for Top Customers")

    # Popular Restaurants Insight
    elif insight_selection == "Popular Restaurants":
        popular_res_query = """
        SELECT restaurant_id, COUNT(order_id) AS order_count
        FROM Orders
        GROUP BY restaurant_id
        ORDER BY order_count DESC
        LIMIT 10
        """
        df = db_ops.fetch_as_dataframe(query=popular_res_query)
        if not df.empty:
            st.write(df)
        else:
            st.error("No data available for Popular Restaurants")

    # Delivery Performance Insight
    elif insight_selection == "Delivery Performance":
        performance_query = """
        SELECT delivery_person_id, AVG(delivery_time) AS avg_delivery_time
        FROM Deliveries
        GROUP BY delivery_person_id
        """
        df = db_ops.fetch_as_dataframe(query=performance_query)
        if not df.empty:
            st.write(df)
        else:
            st.error("No data available for Delivery Performance")
