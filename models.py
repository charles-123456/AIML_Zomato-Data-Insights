import mysql.connector
import streamlit as st
import pandas as pd


class DatabaseOperations:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="charles",
            password="charles@123",
            database="zemato"
        )
        self.cursor = self.db.cursor()

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            self.db.commit()
            st.success("Operation successful!")
        except Exception as e:
            st.error(f"Error: {e}")

    def add_record(self, table_name, column_names, column_values):
        columns = ', '.join(column_names)
        values = ', '.join([f"'{value}'" for value in column_values])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        self.execute_query(query)

    def update_record(self, table_name, column_names, column_values, condition):
        set_clause = ', '.join([f"{col}='{val}'" for col, val in zip(column_names, column_values)])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        self.execute_query(query)

    def delete_record(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.execute_query(query)

    def add_column(self, table_name, column_name, column_type):
        query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}"
        self.execute_query(query)

    def fetch_as_dataframe(self, query):
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            columns = [col[0] for col in self.cursor.description]  # Extract column names
            df = pd.DataFrame(rows, columns=columns)
            return df
        except Exception as e:
            print(f"Error: {e}")
            return pd.DataFrame()