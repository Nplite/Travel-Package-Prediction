from package.pipeline.pipeline import Pipeline
from package.exception import PackageException
from package.logger import logging
from package.config.configuration import Configuration
from package.component.data_ingestion import DataIngestion
import os
def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuration(config_file_path=config_path))
        #pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed.")

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()
