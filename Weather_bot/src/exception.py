import sys
from logger import logging


logging.basicConfig(filename="error.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

def error_message_detail(error,error_detail: sys):
    exc_type,_,exc_tb = error_detail.exc_info() #sys.exc_info() returns a tuple of three values that provide information about the exception that is currently being handled (exception_type, exception_value, traceback_object)
    
    if exc_tb is None:
        return f"Error:{str(error)}"

    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in script[{filename}] at line number [{exc_tb.tb_lineno}]"
    logging.exception(error_message)
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
    
    def __str__(self):
        return self.error_message
