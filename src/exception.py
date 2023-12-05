#library
import sys

#function to obtain error message, line number and script name
def get_error_message(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    #file name
    file_name = exc_tb.tb_frame.f_code.co_filename
    #line number
    line_number = exc_tb.tb_lineno
    #error
    error_ = str(error)
    #error message
    error_message = f"The Exception occured at a script {file_name} in line number {line_number} with an error message of {error_}"
    return error_message

# custom class to raise error
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = get_error_message(error_message, error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message