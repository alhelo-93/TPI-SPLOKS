import sys
from PyQt5 import QtWidgets, uic
import time
from model.client import Customer


def displayCustomers():
    """
        * < displayCustomers >: Function that displays all the clients
        * return: Returns nothing
    """
    global wCustomers
    wCustomers = uic.loadUi('views/clients.ui')  # Load the .ui file
    wCustomers.LblMsgConfirmation.hide()
    wCustomers.btnaddclient.clicked.connect(displayAddNewForm)

    global customer
    customer = Customer()
    wCustomers.tableCustomers.cellClicked.connect(displayDetail)
    loadTableCustomers()
    wCustomers.show()


def loadTableCustomers():
    """
    It will display the data in the table

    param customers: The list of customers that will be displayed in the table
    """
    customers = Customer.all()
    wCustomers.tableCustomers.cellClicked.connect(loadCustomerDetails)
    wCustomers.tableCustomers.setColumnHidden(0, True)  # Set the id's column as hidden
    for row_number, customer in enumerate(customers):  # Loop that will display data in the table
        wCustomers.tableCustomers.insertRow(row_number)  # Insert the amount of rows needed
        for column_number, data in enumerate(customer):
            cell = QtWidgets.QTableWidgetItem(str(data))  # Initializes the variable as a TableWidget with data
            wCustomers.tableCustomers.setItem(row_number, column_number, cell)  # Add data in the cell of the table
            # Opens the customer's details' window when clicked in a cell


def displayDetail():
    """
    It displays the details of one customer using its id
    """
    global w_customer_details
    w_customer_details = uic.loadUi('views/clientsDetails.ui')  # Load the .ui file
    global customer_Id
    customer_Id = wCustomers.tableCustomers.item(wCustomers.tableCustomers.currentRow(), 0).text()  # Get the id of
    # the clicked customer
    customer.load(customer_Id)  # Calls function that loads data of the customer with his id

    w_customer_details.show()  # Show the window


def loadCustomerDetails():
    """
         It loads the customer details into the customer details window
    """
    # show name lastname of client on top of the form
    """"
    """
    # Set label's text with the lastname and firstname as Title
    w_customer_details.lblTitleClient.setText(str(customer.firstname) + "   " + str(customer.lastname))

    w_customer_details.inputLastName.setText(str(customer.lastname))  # Set label's text with the lastname

    w_customer_details.inputFirstName.setText(str(customer.firstname))  # Set label's text with firstname
    w_customer_details.inputaddress.setText(str(customer.address))  # Set label's text with address
    w_customer_details.inputNpa.setText(str(customer.npa))  # Set label's text with NPA and
    w_customer_details.inputTown.setText(str(customer.town))  # town
    w_customer_details.inputMail.setText(str(customer.email))  # Set label's text with email
    w_customer_details.inputMobile.setText(str(customer.mobile))  # Set label's text with mobile number
    w_customer_details.btnHistory.clicked.connect(historyOfModification)
    w_customer_details.btnSave.clicked.connect(UpdateCustomerDetails)
    w_customer_details.btnSave.clicked.connect(refrechCustomerData)
    w_customer_details.btnSave.clicked.connect(closeCurrentDetailsWindow)
    w_customer_details.btnSave.clicked.connect(MsgOfModification)


def UpdateCustomerDetails():
    customer.firstname = w_customer_details.inputFirstName.text()
    customer.lastname = w_customer_details.inputLastName.text()
    customer.address = w_customer_details.inputaddress.text()
    customer.email = w_customer_details.inputMail.text()
    customer.mobile = w_customer_details.inputMobile.text()
    customer.npa = w_customer_details.inputNpa.text()
    customer.town = w_customer_details.inputTown.text()
    updateRecord = [customer.firstname, customer.lastname, customer.address, customer.email, customer.mobile,
                    customer.npa, customer.town]
    customer.updateOne(updateRecord)


def displayAddNewForm():
    global wNewClient
    wNewClient = uic.loadUi('views/newclient.ui')  # Load the .ui file
    wNewClient.btnAddOK.clicked.connect(addNewCustomer)

    wNewClient.show()


def addNewCustomer():
    """
           * < clientForum >: Function that displays new client forum
           * return: Returns nothing
    """

    customer.firstname = wNewClient.inputName.text()
    customer.lastname = wNewClient.inputLastName.text()
    customer.address = wNewClient.inputAddress.text()
    customer.email = wNewClient.inputEmail.text()
    customer.mobile = wNewClient.inputPhone.text()
    customer.town = wNewClient.inputCity.text()
    customer.npa = wNewClient.inputNpa.text()

    newRecord = (
        customer.npa, customer.town, customer.firstname, customer.lastname, customer.address, customer.email,
        customer.mobile,)
    customer.createNew(newRecord)


def closeCurrentWindow():
    wNewClient.close()


def closeCurrentDetailsWindow():
    w_customer_details.close()


def refrechCustomerData():
    loadTableCustomers()


def MsgOfModification():
    wCustomers.LblMsgConfirmation.setText(
        "le client est modifié" + " " + str(customer.firstname) + " " + str(customer.lastname))
    wCustomers.LblMsgConfirmation.show()


def historyOfModification():
    global whistory
    whistory = uic.loadUi('views/historylist.ui')

    loadHistoryOfModification()
    whistory.show()


def loadHistoryOfModification():
    listM = Customer.Historylist()
    for row_number, onehistory in enumerate(listM):
        whistory.tblModifcation.insertRow(row_number)
        for column_number, data in enumerate(onehistory):
            cell = QtWidgets.QTableWidgetItem(str(data))
            whistory.tblModifcation.setItem(row_number, column_number, cell)




