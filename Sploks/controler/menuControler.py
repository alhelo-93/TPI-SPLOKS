from PyQt5 import QtWidgets, QtGui, uic
import sys

from controler import contractsControler as contracts
from controler import staffsControler as staffs


def displayMenu(self):
    global wMenu
    wMenu = uic.loadUi('views/menu.ui', self)  # Load the .ui file
    # wMenu.btnClients.clicked.connect(getClients)  # Open the list of clients
    wMenu.btnStaff.clicked.connect(getStaffs)  # Open the list of staffs
    # wMenu.btnStock.clicked.connect()  # Open the list of item
    wMenu.btnContracts.clicked.connect(getContracts)  # Open the list of item

    wMenu.show()  # Show the menu


def getContracts():
    contracts.displayContracts()


def getStaffs():
    staffs.displayStaffs()
