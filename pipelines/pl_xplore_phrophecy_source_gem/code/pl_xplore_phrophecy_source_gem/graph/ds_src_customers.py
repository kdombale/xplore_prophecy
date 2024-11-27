from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_xplore_phrophecy_source_gem.config.ConfigStore import *
from pl_xplore_phrophecy_source_gem.functions import *

def ds_src_customers(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("Id", StringType(), True), StructField("OwnerId", StringType(), True), StructField("IsDeleted", StringType(), True), StructField("Name", StringType(), True), StructField("CreatedDate", StringType(), True), StructField("CreatedById", StringType(), True), StructField("LastModifiedDate", StringType(), True), StructField("LastModifiedById", StringType(), True), StructField("SystemModstamp", StringType(), True), StructField("PartyId", StringType(), True), StructField("TotalLifeTimeValue", StringType(), True), StructField("CustomerStatusType", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/tmp/customers.csv")
