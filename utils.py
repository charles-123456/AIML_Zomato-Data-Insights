import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
import streamlit as st


# # def get_peak_times():
# #     query = """
# #     SELECT HOUR(order_date) AS hour, COUNT(*) AS order_count
# #     FROM Orders
# #     GROUP BY HOUR(order_date)
# #     ORDER BY order_count DESC
# #     """
# #     df = pd.read_sql(query, con=db)
# #     return df


def plot_peak_times(df):
    st.title("Peak Ordering Times")
    sns.barplot(x='hour', y='order_count', data=df)
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of Orders")
    st.pyplot()


# def get_delayed_orders():
#     query = """
#     SELECT * FROM Deliveries
#     WHERE delivery_time > estimated_time
#     """
#     df = pd.read_sql(query, con=db)
#     return df


# def get_top_customers():
#     query = """
#     SELECT customer_id, COUNT(order_id) AS order_count, SUM(total_amount) AS total_spent
#     FROM Orders
#     GROUP BY customer_id
#     ORDER BY order_count DESC
#     LIMIT 10
#     """
#     df = pd.read_sql(query, con=db)
#     return df


# def track_delivery_performance():
#     query = """
#     SELECT delivery_person_id, AVG(delivery_time) AS avg_delivery_time
#     FROM Deliveries
#     GROUP BY delivery_person_id
#     """
#     df = pd.read_sql(query, con=db)
#     return df

# def get_popular_restaurants():
#     query = """
#     SELECT restaurant_id, COUNT(order_id) AS order_count
#     FROM Orders
#     GROUP BY restaurant_id
#     ORDER BY order_count DESC
#     LIMIT 10
#     """
#     df = pd.read_sql(query, con=db)
#     return df

