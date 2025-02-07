# set the RDD (resilient Distributed Database) to the sc (spark context, entry point for working with RDD's)
# parallelize the list of numbers 1-5 to the RDD across the cluster of nodes
# this creates a distributed dataset that can be operated on in parallel

# start the session:
pyspark

rdd = sc.parallelize([1, 2, 3, 4, 5]) 

# Now rdd is the RDD object that we can perform operations on
# which is the data structure of the list of numbers 1-5 distributed across the cluster of nodes
# these numbers could be larger data sets, such as a list of all the words in a book, or all the data in a database

# The map() function in Apache Spark is a transformation that applies a function to each element in an RDD
# and returns a new RDD representing the results.

# The lambda function x: x * x is applied to each element in the RDD rdd
# and returns a new RDD with the squared values
squared = rdd.map(lambda x: x * x)

# to see the result of the map transformation, we can call the collect() action on the new RDD
squared.collect()

# we can also do things to the RDD like sum all the elements
rdd.sum()

# Strings
# we can have a list of strings
rdd = sc.parallelize(["hello", "world", "goodbye", "world"])

# we can manipulate the strings in the same way as numbers
split = rdd.map(lambda x: x.split("o")) # spits up the data into a list of strings around "o"

# moving to more advanced operations, we can use the flatMap() function
# which is similar to map, but returns a flattened list of results
# so if we have a list of lists, it will return a single list
# for example, if we have a list of strings, it will return a single list of strings
# instead of a list of lists of strings
# this is useful for splitting up strings into individual words
words = rdd.flatMap(lambda x: x.split("o"))

