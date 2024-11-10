import sqlite3
import pandas as pd
import os
# Path to db
db_path = r'C:\Users\14042\Downloads\grocery_db.sqlite'

# Connect to the SQLite database
conn = sqlite3.connect(db_path)

# List of SQL queries
queries = [
    "SELECT SUM(Total) AS total_sales FROM supermarket_sales;",  # Aggregation: total sales
    "SELECT branch, SUM(Total) AS total_sales FROM supermarket_sales GROUP BY branch ORDER BY total_sales DESC;",  # Sales by Branch
    "SELECT product_line, AVG(Rating) AS average_rating FROM supermarket_sales GROUP BY product_line ORDER BY average_rating DESC;",  # Average Rating by Product Line
    "SELECT customer_type, SUM(Total) AS total_sales FROM supermarket_sales GROUP BY customer_type;",  # Total Sales by Customer Type
    "SELECT product_line, SUM(Total) AS total_sales FROM supermarket_sales GROUP BY product_line ORDER BY total_sales DESC LIMIT 5;",  # Top 5 Products with Highest Sales
    "SELECT payment_method, SUM(Total) AS total_sales FROM supermarket_sales GROUP BY payment_method ORDER BY total_sales DESC;",  # Sales per Payment Method
    "SELECT gender, SUM(Total) AS total_sales FROM supermarket_sales GROUP BY gender;"  # Sales by Gender
]

# Set the directory for saving CSV files
output_directory = r'C:\Users\14042\Downloads'

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Execute each query and export the results to separate CSV files
for i, query in enumerate(queries, start=1):
    # Run the query and fetch results into a DataFrame
    df = pd.read_sql(query, conn)

    # Define the full path for the CSV output file
    csv_output_path = os.path.join(output_directory, f"query_result_{i}.csv")

    # Export the DataFrame to a CSV file
    df.to_csv(csv_output_path, index=False, encoding='utf-8')
    print(f"Query {i} result exported to {csv_output_path}")

# Close the database connection
conn.close()