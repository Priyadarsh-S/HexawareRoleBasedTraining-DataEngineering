What is RDD?

RDD (Resilient Distributed Dataset) is the fundamental data structure in Spark. It is an immutable collection of data that is distributed across multiple nodes and processed in parallel.

Example:

&#x09;rdd = sc.parallelize(\[1, 2, 3, 4, 5])



What's the advantage of using RDD?

* Fault Tolerant – Can recover lost data using lineage.
* Distributed Processing – Data is processed across multiple machines.
* Scalable – Handles very large datasets.
* In-Memory Processing – Faster than disk-based processing.
* Immutable – Original data cannot be modified accidentally.



What is Lazy Evaluation?

Lazy Evaluation means Spark does not execute transformations immediately. It records them and executes only when an action is called.

Example:

&#x09;rdd1 = rdd.map(lambda x: x \* 2)      # Transformation

&#x09;rdd2 = rdd1.filter(lambda x: x > 5)  # Transformation



&#x09;rdd2.collect()                       # Action

Here, map() and filter() are not executed until collect() is called.

Advantage: Spark can optimize the execution plan, improving performance.

