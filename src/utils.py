import sys





def get_requirements(file_path:str)->list:
  """
    This function will read the content of the provided file which should be the requirements.txt
    It will return a list of the packages that are required for the project to run
    ex: ['numpy', 'pandas', 'sklearn']

    The reason that this function is being used is because the requirements.txt file might contain
    the line "-e ." which is used to install the package as a editable package. This is not needed
    when installing the package using pip, so we need to remove it from the requirements.txt file
    before installing the package using pip.

    The function will also remove the new line character from each line in the file because
    the readlines() method will return a list of strings with the new line character at the end of each string
  """
  requirements = []
  with open(file_path) as file_obj:
    requirements = file_obj.readlines()
    requirements = [req.replace("\n","") for req in requirements]

    if ('-e .') in requirements:
      requirements.remove('-e .')

  return requirements


def error_message_detail(error, error_detail:sys):
  """
    This function will create a detail of the error message that occurs in the code
    It will return a string that will indicate the file name, line number and the error message
    ex: Error occured in python script name [main.py] line number [16] error message [list index out of range]
  """
  #get the information of the error
  _,_,exc_tb = error_detail.exc_info()
  
  #get the file name where the error occur
  file_name = exc_tb.tb_frame.f_code.co_filename

  #get the line number where the error occur
  error_line_number = exc_tb.tb_lineno

  #get the error message
  error_message = str(error)

  #create the detail of the error message
  error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name, error_line_number, error_message
  )

  #return the error message
  return error_message
