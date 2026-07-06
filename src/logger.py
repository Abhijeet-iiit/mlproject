import logging
import os 
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,)

    
# def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
#     """
#     Set up a logger with the specified name and level.

#     Args:
#         name (str): The name of the logger.
#         level (int): The logging level (default is logging.INFO).

#     Returns:
#         logging.Logger: Configured logger instance.
#     """
#     logger = logging.getLogger(name)
#     logger.setLevel(level)

#     # Create console handler and set level
#     ch = logging.StreamHandler()
#     ch.setLevel(level)

#     # Create formatter and add it to the handler
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     ch.setFormatter(formatter)

#     # Add the handler to the logger
#     if not logger.handlers:
#         logger.addHandler(ch)

#     return logger