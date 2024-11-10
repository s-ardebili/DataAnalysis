# DataAnalysis

This project demonstrates data analysis and visualization by using SQL, Python, and Tableau. It covers data extraction and the visualization of supermarket sales, taken from a dataset from Kabble.

Files:

GroceryQueries.sql: SQL script to create and populate a MySQL database with supermarket sales data.
GrocerySales.py: This Python script connects to a SQLite database (grocery_db.sqlite) I created, which contains supermarket sales data and performs various analyses. Using a series of SQL queries, it retrieves insights such as:total sales, sales breakdowns by different categories, and top performing products. This file also makes each query's result be saved as a separate file.
Excel.py: This Python script combines data from multiple .xlsx files within a directory into a single Excel file. For each .xlsx file, it reads all sheets, adds a Source_File column to track the original file, and writes each sheet to a new sheet in the combined file. 
GroceryVisual.twb: Open this file for visual representations of each query.





