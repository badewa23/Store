import logging

class Log:
    
    def __init__(self, log_file_name: str = "Store.log"):
        try:
            logging.basicConfig(filename = log_file_name, level = logging.DEBUG, 
                                format='%(asctime)s :: %(message)s')
        except:
            print("Could not create log")
    
    def add_logging_info(self,info: str):
        logging.info(info)
        
    def add_logging_error(self,error: str):
        logging.error(error)