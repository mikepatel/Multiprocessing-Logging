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

    team = Team(ticket=ticket, log_filename=log_filename)
    player = Player(ticket=ticket, log_filename=log_filename)


################################################################################
# Main
if __name__ == "__main__":
    tickets = [i for i in range(10)]

    processes = Pool(processes=len(tickets))
    processes.map(run, tickets)
    processes.close()
