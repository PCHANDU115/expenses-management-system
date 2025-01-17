# Personal-expenses-management-system


# Purpose
The Expense Tracker Application is designed to help users efficiently track and visualize their expenses over time. With features to add custom expenses, filter expenses by date, and view detailed expense summaries through visualizations, it empowers users to manage their finances effectively.

# Technologies and Libraries Used
Programming Language: Python
GUI Library: Tkinter
Database: SQLite3
Data Analysis: Pandas
Data Visualization: Matplotlib, Seaborn
# Objective
Provide users with a simple and intuitive interface to log their daily expenses.
Categorize and store expense details (description, category, amount, and date) in a database.
Allow users to filter expenses within a specific date range.
Display interactive bar charts summarizing expenses by category.
# Implementation Steps
# 1.Database Setup:

A SQLite database is created to store expenses.
A table named expenses is used to store the following fields: description, category, amount, and date.
# 2.Expense Addition:

Users can input expense details (category, amount, and date) via a form.
The data is validated and stored in the database.
# 3.Date Range Filtering:

Users can specify a start and end date to fetch expenses within that range.
The filtered data is retrieved from the database for further processing.
# 4.Data Visualization:

Expenses are visualized as a bar chart using Matplotlib and Seaborn.
The graph displays total expenses by category, providing insights into spending patterns.
# 5.User Interface:

A user-friendly Tkinter-based GUI facilitates seamless data input and visualization.
Interactive buttons and input fields allow easy navigation and operation.
