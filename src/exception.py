import sys 
from .utils import error_message_detail
from .logger import Logger

class CustomException(Exception):
  """
    This is a custom exception class that we will use to handle all the exception that will occur in our code
    We will use this class to create a custom exception that will give us the error message and the detailed error message
    The detailed error message will include the file name, line number and the error message
    ex: Error occured in python script name [main.py] line number [16] error message [list index out of range]
  """
  def __init__(self, error_message, error_detail:sys):
    """
      This is the constructor of the class, it will take in the error message and the error detail
      The error detail is a sys class that will give us the information about the error
      ex: error_detail = sys.exc_info()
    """
    super().__init__(error_message)
    """
      This will call the constructor of the parent class and will set the error message
    """
    self.error_message = error_message_detail(error_message, error_detail)
    """
      This will call the function error_message_detail and will pass in the error message and the error detail
      The function will return a string that will include the file name, line number and the error message
    """
  def __str__(self):
    """
      This is a special method in python that will return a string representation of the object
      In this case, it will return the error message
    """
    return self.error_message
  
if __name__ == "__main__":
  logger = Logger()
  try:
    a = 1/0
  except Exception as e:
    logger.error(e)
    raise CustomException(e, sys)
   
