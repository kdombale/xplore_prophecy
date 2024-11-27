from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_xplore_phrophecy_source_gem.config.ConfigStore import *
from pl_xplore_phrophecy_source_gem.functions import *
from prophecy.utils import *
from pl_xplore_phrophecy_source_gem.graph import *

def pipeline(spark: SparkSession) -> None:
    df_ds_src_customers = ds_src_customers(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_xplore_phrophecy_source_gem")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_xplore_phrophecy_source_gem")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_xplore_phrophecy_source_gem", config = Config)(
        pipeline
    )

if __name__ == "__main__":
    main()
