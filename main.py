# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

# STEP 2
# employee number and last name
df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName
FROM employees
""", conn)

# STEP 3
# same columns, order swapped
df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber
FROM employees
""", conn)

# STEP 4
# employee number renamed to ID
df_alias = pd.read_sql("""
SELECT lastName, employeeNumber AS ID
FROM employees
""", conn)

# STEP 5
# flag each employee as executive or not
df_executive = pd.read_sql("""
SELECT
    employeeNumber,
    lastName,
    firstName,
    jobTitle,
    CASE
        WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing') THEN 'Executive'
        ELSE 'Not Executive'
    END AS role
FROM employees
""", conn)

# STEP 6
# character count of each last name
df_name_length = pd.read_sql("""
SELECT LENGTH(lastName) AS name_length
FROM employees
""", conn)

# STEP 7
# first two letters of each job title
df_short_title = pd.read_sql("""
SELECT SUBSTR(jobTitle, 1, 2) AS short_title
FROM employees
""", conn)

# STEP 8
# total value of all order lines
sum_total_price = pd.read_sql("""
SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total_price
FROM orderdetails
""", conn).sum().reset_index(drop=True)

# STEP 9
# split order date into day, month and year
df_day_month_year = pd.read_sql("""
SELECT
    orderDate,
    CAST(strftime('%d', orderDate) AS TEXT) AS day,
    CAST(strftime('%m', orderDate) AS TEXT) AS month,
    CAST(strftime('%Y', orderDate) AS TEXT) AS year
FROM orders
""", conn)

conn.close()