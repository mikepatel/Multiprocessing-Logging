"""


"""
################################################################################
# Imports
from logger import Logger


################################################################################
class Player:
    def __init__(self, ticket, log_filename):
        self.logger = Logger(__name__, log_filename).get_logger()
        self.logger.info(f'{ticket}')
