"""


"""
################################################################################
# Imports
from multiprocessing import Pool

from logger import Logger
from team import Team
from player import Player


################################################################################
# helper function
def run(ticket):
    ticket = str(ticket)
    log_filename = ticket + ".txt"

    logger = Logger(ticket, log_filename).get_logger()

    team = Team(ticket=ticket, logger=logger)
    player = Player(ticket=ticket, logger=logger)


################################################################################
# Main
if __name__ == "__main__":
    tickets = [i for i in range(10)]

    processes = Pool(processes=len(tickets))
    processes.map(run, tickets)
    processes.close()
