# Compared to RDD's, DataFrames are for structured data and are more efficient.

from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("DataFrameExample").getOrCreate()
# this is the entry point to programming Spark with the Dataset and DataFrame API

# Create DataFrame from list
df = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"]) # need to have ["column_name_1", "column_name_2", ...] as the second argument

# Show the DataFrame
df.show()

# Apply transformations 
df_filtered = df.filter(df.id > 1) # filter out the rows where the id is less than 1
df_filtered.show()
