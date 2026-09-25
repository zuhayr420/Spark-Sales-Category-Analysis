from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, col

# Create Spark session
spark = SparkSession.builder \
    .appName("Sales Category Analysis") \
    .getOrCreate()

# Load sales dataset
df = spark.read.csv(
    "Superstore_Sales.csv",
    header=True,
    inferSchema=True
)

# Display dataset
print("Sales Dataset:")
df.show(5)

# Calculate products sold in each category
result = df.groupBy("Category") \
    .agg(sum("Quantity").alias("Total_Products_Sold")) \
    .orderBy("Category")

# Display result
print("Products Sold in Each Category:")
result.show()

# Save result
result.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("output")

# Stop Spark
spark.stop()
