import requests
from bs4 import BeautifulSoup
from src.logger import Logger
from tqdm import tqdm
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class DataScraperConfig:
    """
    Configuration class for the DataScraper.
    """
    logger: Logger
    data_path: str = os.path.join('artifacts', 'scrapped_data.csv')
    input_file: str = os.path.join('src', 'Notebook', 'Data', 'autos.csv')  # Use forward slashes
    data: pd.DataFrame = field(default_factory=pd.DataFrame, init=False)  # Initialize as empty DataFrame

    def __post_init__(self):
        """
        Load data after the dataclass is initialized.
        """
        self.data = self._load_data()

    def _load_data(self) -> pd.DataFrame:
        """
        Load data from the input file and handle errors.
        """
        try:
            df = pd.read_csv(self.input_file, parse_dates=['dateCrawled', 'lastSeen', 'dateCreated'])
            self.logger.info(f"Data successfully loaded from {self.input_file}")
            return df
        except FileNotFoundError:
            self.logger.error(f"File not found: {self.input_file}")
            raise
        except Exception as e:
            self.logger.error(f"Error loading data from {self.input_file}: {e}")
            raise


class DataScraper:
    """
    This class handles the scraping of vehicle types for car models.
    It uses the custom Logger for logging and includes custom exception handling.
    """
    def __init__(self, config: DataScraperConfig):
        """
        Initialize the DataScraper with the configuration.
        """
        self.config = config
        self.not_found = []
        self.found = []

    def fetch_vehicle_type(self, car_model):
        """
        Fetch the vehicle type for a given car model from the website.
        """
        try:
            web = requests.get(f'https://www.auto-data.net/en/results?search={car_model}')
            web.raise_for_status()  # Raise an exception for HTTP errors
            soup = BeautifulSoup(web.content, 'html.parser')
            v_type = soup.find('span', class_='additional').find('strong').text
            self.config.logger.info(f'Found: {car_model}')
            self.found.append(car_model)
            return car_model, v_type
        except requests.exceptions.RequestException as e:
            self.config.logger.error(f'Could not fetch data for {car_model}: {e}')
            self.not_found.append(car_model)
            return car_model, None
        except AttributeError:
            self.config.logger.warning(f'Vehicle type not found for {car_model}')
            self.not_found.append(car_model)
            return car_model, None

    def update_dataframe(self, results):
        """
        Update the DataFrame with the fetched vehicle types.
        """
        for car_model, v_type in results:
            if v_type:
                self.config.data.loc[self.config.data['car_model'] == car_model, 'vehicleType'] = v_type

    def scrape_data(self):
        """
        Perform the scraping process using ThreadPoolExecutor for concurrent requests.
        """
        all_cars = self.config.data.loc[self.config.data['vehicleType'].isnull(), 'car_model'].str.lower().tolist()

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(self.fetch_vehicle_type, model) for model in all_cars]
            results = []
            for future in tqdm(as_completed(futures), total=len(all_cars)):
                results.append(future.result())

        # Update the DataFrame with the fetched vehicle types
        self.update_dataframe(results)

        # Log the results
        self.config.logger.info(f"Found: {self.found}")
        self.config.logger.warning(f"Not found: {self.not_found}")

        # Save the updated DataFrame to the specified path
        os.makedirs(os.path.dirname(self.config.data_path), exist_ok=True)
        self.config.data.to_csv(self.config.data_path, index=False)
        self.config.logger.info(f"Data saved to {self.config.data_path}.")


if __name__ == "__main__":
    logger = Logger()
    logger.info("Starting DataScraper...")