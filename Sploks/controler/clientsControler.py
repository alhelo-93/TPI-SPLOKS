from PyQt5 import QtWidgets, uic, QtCore
from model.client import Customer


def displayCustomers():
    """
        * < displayCustomers >: Function that displays all the clients
        * return: Returns nothing
    """
    global wCustomers
    wCustomers = uic.loadUi('views/clients.ui')  # Load the .ui file
    wCustomers.btnaddclient.clicked.connect(addNewCustomer)

    global customer
    customer = Customer()
    wCustomers.tableCustomers.cellClicked.connect(displayDetail)
    loadTableCustomers(customer.all())
    wCustomers.show()


def displayDetail():
    """
    It displays the details of one customer using its id
    """
    global w_customer_details
    w_customer_details = uic.loadUi('views/clientsDetails.ui')  # Load the .ui file
    global customer_Id
    customer_Id = wCustomers.tableCustomers.item(wCustomers.tableCustomers.currentRow(),
                                                 0).text()  # Get the id of the clicked customer
    customer.load(customer_Id)  # Calls function that loads data of the customer with his id
    loadCustomerDetails()  # Calls function that displays the data in window with lastname and firstname as customer's identifier
    w_customer_details.show()  # Show the window


def loadTableCustomers(customers):
    """
    It will display the data in the table

    :param customers: The list of customers that will be displayed in the table
    """
    wCustomers.tableCustomers.setColumnHidden(0, True)  # Set the id's column as hidden
    for row_number, customer in enumerate(customers):  # Loop that will display data in the table
        wCustomers.tableCustomers.insertRow(row_number)  # Insert the amount of rows needed
        for column_number, data in enumerate(customer):
            cell = QtWidgets.QTableWidgetItem(str(data))  # Initializes the variable as a TableWidget with data
            wCustomers.tableCustomers.setItem(row_number, column_number, cell)  # Add data in the cell of the table
            wCustomers.tableCustomers.cellClicked.connect(
                loadCustomerDetails)  # Opens the customer's details' window when clicked in a cell


def loadCustomerDetails():
    """
         It loads the customer details into the customer details window
    """
    # show name lastname of client on top of the form
    w_customer_details.lblTitleClient.setText(str(customer.firstname)+" "+str(customer.lastname))
    w_customer_details.lblNom.setText(str(customer.lastname))  # Set label's text with the lastname
    w_customer_details.lblPrenom.setText(str(customer.firstname))  # Set label's text with firstname
    w_customer_details.lblAdresse.setText(str(customer.address))  # Set label's text with address
    w_customer_details.lblNPA.setText(str(customer.npa) + " " + str(customer.town))  # Set label's text with NPA and town
    w_customer_details.lblEmail.setText(str(customer.email))  # Set label's text with email
    w_customer_details.lblNumero.setText(str(customer.mobile))  # Set label's text with mobile number


def addNewCustomer():
    """
           * < clientForum >: Function that displays new client forum
           * return: Returns nothing
       """
    global wNewClient
    wNewClient = uic.loadUi('views/newclient.ui')  # Load the .ui file
    wNewClient.show()
