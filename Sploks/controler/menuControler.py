from PyQt5 import QtWidgets, QtGui, uic
import sys

from controler import clientsControler as clients
from controler import staffsControler as staffs
from controler import contractsControler as contracts


def displayMenu(self):
    global wMenu
    wMenu = uic.loadUi('views/menu.ui', self)  # Load the .ui file
    # wMenu.btnClients.clicked.connect(getClients)  # Open the list of clients
    wMenu.btnClients.clicked.connect(getClients)
    # wMenu.btnStaff.clicked.connect() # Open the list of staffs
    wMenu.btnStaff.clicked.connect(getStaffs)
    # wMenu.btnContracts.clicked.connect()  # Open the list of Contracts
    wMenu.btnContracts.clicked.connect(getContracts)

    wMenu.show()  # Show the menu


def getClients():
    clients.displayClients()


def getStaffs():
    staffs.displayStaffs()

def getContracts():
    contracts.displayContracts()



