
import os
import logging
from datetime import datetime
import inspect

class Logger:
    """
    This class will create a new logger every time it is initialized.
    The logger will be used to log information into a file.
    The log file will be created in the current working directory in a folder named logs.
    The log file will be named after the file in which the Logger is initialized.
    The date and time will be included as part of the log content.
    """
    def __init__(self):
        """
        This function will create a new logger.
        """
        # Get the name of the file where the Logger is initialized
        caller_frame = inspect.stack()[1]
        caller_filename = os.path.basename(caller_frame.filename).split(".")[0]  # Get filename without extension

        # Create the log file name using the caller's filename
        self.LOG_FILE = f"{caller_filename}.log"

        # Define the logs directory path
        self.logs_path = os.path.join(os.getcwd(), "logs")
        os.makedirs(self.logs_path, exist_ok=True)

        # Define the full log file path
        self.LOG_FILE_PATH = os.path.join(self.logs_path, self.LOG_FILE)

        # Configure logging
        logging.basicConfig(
            filename=self.LOG_FILE_PATH,
            format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
            level=logging.INFO
        )

    def error(self, message):
        """
        This function will log an error message.
        """
        logging.error(message)

    def info(self, message):
        """
        This function will log an info message.
        """
        logging.info(message)

    def warning(self, message):
        """
        This function will log a warning message.
        """
        logging.warning(message)

    def debug(self, message):
        """
        This function will log a debug message.
        """
        logging.debug(message)


if __name__ == "__main__":
    logger = Logger()
    logger.error("This is an error message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.debug("This is a debug message")

