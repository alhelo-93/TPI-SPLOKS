from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem

from const import con

from model.contract import Contract


def displayContracts():
    """
        * < displayContracts >: Function that displays all the Contracts
        * return: Returns nothing
    """
    global wContracts
    wContracts = uic.loadUi('views/Contracts.ui')  # Load the .ui file
    ##
    global contract
    contract = Contract()
    loadData()
    wContracts.show()  # Show the window


def loadData():
    contracts = Contract.all()
    wContracts.tableContracts.setColumnHidden(0, True)
    for row_number, contract in enumerate(contracts):
        wContracts.tableContracts.insertRow(row_number)
        for column_number, data in enumerate(contract):
            cell: QTableWidgetItem = QtWidgets.QTableWidgetItem(str(data))
            wContracts.tableContracts.setItem(row_number, column_number, cell)




