import logging
import os
from datetime import datetime
#  It's an way to record events
#  during the execution of the programm,
#  like the error in the custome excetion handling etc.

LOG_File=f"{datetime.now().strftime('%m_%d_%Y_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_File)
os.makedirs(log_path,exist_ok=True)

LOG_File_PATH=os.path.join(log_path,LOG_File)

logging.basicConfig(
    filename=LOG_File_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s-%(levelname)s-%(message)s", 
    level=logging.INFO



)
