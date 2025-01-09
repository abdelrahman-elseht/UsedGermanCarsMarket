import os
import sys
from src.exception import CustomException
from src.logger import Logger
from sklearn.model_selection import train_test_split
import pandas as pd
from dataclasses import dataclass
from src.components.DataScraping import DataScraper, DataScraperConfig


@dataclass
class DataIngestionConfig:
    scraped_data_path: str = os.path.join('artifacts', 'scrapped_data.csv')
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logger = Logger()
        logger.info('Data Ingestion started')
        try:
            df = pd.read_csv(self.ingestion_config.scraped_data_path, parse_dates=['dateCrawled', 'lastSeen', 'dateCreated'])
            logger.info("Read the Scraped dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logger.info('Train test split started')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logger.info("Ingestion of data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)


if __name__ == '__main__':
    logger = Logger()
    logger.info("Scraping for Data Ingestion started")

    try:
        config = DataScraperConfig(logger=logger)
        scraper = DataScraper(config)
        scraper.scrape_data()
    except Exception as e:
        logger.error(e)
        raise CustomException(e, sys)

    try:
        logger.info("Data Ingestion started")
        obj = DataIngestion()
        train_data_path, test_data_path, raw_data_path = obj.initiate_data_ingestion()
    except Exception as e:
        logger.error(e)
        raise CustomException(e, sys)