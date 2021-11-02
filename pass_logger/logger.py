"""


"""
################################################################################
# Imports
import logging


################################################################################
class Logger:
    def __init__(self, name, filename):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # create handlers
        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # create formatters
        # https://docs.python.org/3/library/logging.html#logrecord-attributes
        prefix = f'%(asctime)s - %(name)s - %(levelname)s - '
        base = f'Module: %(module)s | Function: %(funcName)s | Line number: %(lineno)d | Message: %(message)s'
        formatter = logging.Formatter(fmt=prefix+base)

        # add formatters to handlers
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    #
    def get_logger(self):
        return self.logger
