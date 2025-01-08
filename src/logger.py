import logging
import os
from datetime import datetime

class Logger:
    """
    This class will create a new logger every time it is initialized
    The logger will be used to log the information into a file
    The log file will be created in the current working directory in a folder named logs
    The log file will be named after the date and time it was created
    """
    def __init__(self):
        """
        This function will create a new logger
        """
        self.LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        self.logs_path=os.path.join(os.getcwd(),"logs",self.LOG_FILE)
        os.makedirs(self.logs_path,exist_ok=True)

        self.LOG_FILE_PATH=os.path.join(self.logs_path,self.LOG_FILE)

        logging.basicConfig(
          filename=self.LOG_FILE_PATH,
          format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
          level=logging.INFO
        )
    def error(self,message):
        """
        This function will log an error message
        """
        logging.error(message)

    def info(self,message):
        """
        This function will log an info message
        """
        logging.info(message)

    def warning(self,message):
        """
        This function will log a warning message
        """
        logging.warning(message)

    def debug(self,message):
        """
        This function will log a debug message
        """
        logging.debug(message)


if __name__ == "__main__":
    logger = Logger()
    logger.error("this is an error message")
    logger.info("this is an info message")
    logger.warning("this is a warning message")
    logger.debug("this is a debug message")

