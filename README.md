# Description:
This project uses Apache Spark (PySpark) to analyze real-world sales data and calculate the total number of products sold in each product category.

# Objective:

* Load sales data into Spark.
* Group products according to their category.
* Calculate the total quantity of products sold in each category.
* Display the results using Spark DataFrame operations.

# Dataset:

The project uses a Superstore Sales dataset containing sales transaction information such as:

* Category
* Sub-Category
* Product Name
* Quantity
* Sales
* Discount
* Profit

# The dataset should be saved as:

Superstore_Sales.csv

# Technologies Used

* Python
* Apache Spark
* PySpark
* Spark DataFrame

# Installation

Install PySpark using:

pip install pyspark

Or:

pip install -r requirements.txt

# How to Run

Run the program using:

spark-submit spark_category_sales.py 

# Result

The Spark program successfully calculates the total number of products sold in each category using the sales dataset.
