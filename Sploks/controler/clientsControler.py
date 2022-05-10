from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem


def displayClients():
    """
            * < displayCustomers >: Function that displays all the clients
            * return: Returns nothing
        """
    global wClients
    wClients = uic.loadUi('views/customers.ui')  # Load the .ui file
