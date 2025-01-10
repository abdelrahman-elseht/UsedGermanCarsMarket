
import sys,os
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import Logger
from dataclasses import dataclass, field


@dataclass
class FeatureEngineeringConfig:
    logger: Logger
    input_file: str = os.path.join('autos.csv')
    data_path: str = os.path.join('artifacts', 'Feature_Engineered_Data.csv')
    data: pd.DataFrame = field(default_factory=pd.DataFrame, init=False)
    def __post_init__(self):
        self.data = self._load_data()
    def _load_data(self):
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

class FeatureEngineering:
    def __init__(self, config: FeatureEngineeringConfig):
        self.config = config

    
    def assign_season(self, month):
        if 3 <= month <= 5:
            return 'Spring'
        elif 6 <= month <= 8:
            return 'Summer'
        elif 9 <= month <= 11:
            return 'Autumn'
        else:
            return 'Winter'
    
    def save_data(self):
        try:
            os.makedirs(os.path.dirname(self.config.data_path), exist_ok=True)
            self.config.data.to_csv(self.config.data_path, index=False)
            self.config.logger.info(f"Data saved to {self.config.data_path}.")
        except Exception as e:
            self.config.logger.error(f"Error saving data to {self.config.data_path}: {e}")
            raise


    def feature_engineering(self):
        try:
            self.config.logger.info("Feature Engineering started")
            df = self.config.data

            df.rename(columns={'dateCrawled':'dateCrawled','name':'car_model',
                   'yearOfRegistration':'car_creation_year','powerPS':'power_HP',
                   'monthOfRegistration':'car_creation_month',
                   'notRepairedDamage':'unrepaired_damage','dateCreated':'dateCreated','nrOfPictures':'num_pictures',
                   'lastSeen':'sold_date'},inplace=True)
            df['vehicleType']=df['vehicleType'].map({'andere':'other','limousine':'Sedan','kleinwagen':'Hatchback','kombi':'Station wagon (estate)','cabrio':'Cabriolet','coupe':'Coupe','bus':'Van','suv':'Suv'})
            df['gearbox']=df['gearbox'].map({'manuell':'Manual','automatik':'Automatic'})
            df['fuelType']=df['fuelType'].map({'benzin':'Petrol','diesel':'Diesel','lpg':'LPG','andere':'Other','hybrid':'Hybrid','elektro':'Electric'})
            df['unrepaired_damage']=df['unrepaired_damage'].map({'nein':'No','ja':'Yes'})
            df.drop(columns=['index','num_pictures'],axis=1,inplace=True)
            df.drop(columns=['seller','offerType','dateCrawled'],axis=1,inplace=True)
            df['ad_duration_days']=(df['sold_date']-df['dateCreated']).dt.days
            df.drop(columns=['car_creation_month'],axis=1,inplace=True)
            df=df.query('car_creation_year > 1980 and car_creation_year < 2017')
            df['car_age_listed']=(df['dateCreated'].dt.year)-(df['car_creation_year'])
            df.rename(columns={'car_age_listed':'car_age_listed_years'},inplace=True)
            df['car_age_listed']=(df['dateCreated'].dt.year)-(df['car_creation_year'])
            df.reset_index(drop=True,inplace=True)
            df['kilometer_year'] = np.where(df['car_age_listed_years'] != 0, df['kilometer'] / df['car_age_listed_years'], 0)
            df=df.query('kilometer_year < 65000')
            df['season'] = df['dateCreated'].dt.month.apply(self.assign_season)

        except Exception as e:
            self.config.logger.error(f"Error in feature engineering: {e}")
            raise
        try:
            self.config.logger.info("Feature Engineering completed")
            self.save_data()
            self.config.logger.info("Data saved to artifacts folder")
        except Exception as e:
            self.config.logger.error(f"Error saving data: {e}")
            raise
        return df

if __name__ == '__main__':
    logger = Logger()
    logger.info("Feature Engineering called")
    try:
        config = FeatureEngineeringConfig(logger=logger)
        fe = FeatureEngineering(config)
        fe.feature_engineering()
    except Exception as e:
        logger.error(e)
        raise CustomException(e, sys)