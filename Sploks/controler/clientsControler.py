from PyQt5 import QtWidgets, uic

from model.client import Customer


def displayCustomers():
    """
        * < displayCustomers >: Function that displays all the clients
        * return: Returns nothing
    """
    global wCustomers
    wCustomers = uic.loadUi('views/clients.ui')  # Load the .ui file
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
    w_customer_details.lblTitleClient.setText(str(customer.firstname) + " " + str(customer.lastname))
    w_customer_details.inputLastName.setText(str(customer.lastname))  # Set label's text with the lastname
    w_customer_details.inputFirstName.setText(str(customer.firstname))  # Set label's text with firstname
    w_customer_details.inputaddress.setText(str(customer.address))  # Set label's text with address
    w_customer_details.lblNPA.setText(str(customer.npa) + " " + str(customer.town))  # Set label's text with NPA and
    # town
    w_customer_details.inputMail.setText(str(customer.email))  # Set label's text with email
    w_customer_details.inputMobile.setText(str(customer.mobile))  # Set label's text with mobile number
    w_customer_details.btnSave.clicked.connect(UpdateCustomerDetails)
    w_customer_details.btnSave.clicked.connect(refrechCustomerData)
    w_customer_details.btnSave.clicked.connect(closeCurrentDetailsWindow)


def UpdateCustomerDetails():
    customer.firstname = w_customer_details.inputFirstName.text()
    customer.lastname = w_customer_details.inputLastName.text()
    customer.address = w_customer_details.inputaddress.text()
    customer.email = w_customer_details.inputMail.text()
    customer.mobile = w_customer_details.inputMobile.text()

    updateRecord = [customer.firstname, customer.lastname, customer.address, customer.email, customer.mobile]

    customer.updateOne(updateRecord)


def displayAddNewForm():
    global wNewClient
    wNewClient = uic.loadUi('views/newclient.ui')  # Load the .ui file
    wNewClient.btnAddOK.clicked.connect(addNewCustomer)
    wNewClient.btnAddOK.clicked.connect(displayCustomers)
    wNewClient.btnAddOK.clicked.connect(closeCurrentWindow)
    wNewClient.show()


def addNewCustomer():
    """
           * < clientForum >: Function that displays new client forum
           * return: Returns nothing
    """

    customer.firstname = wNewClient.inputName.text()
    customer.lastname = wNewClient.inputLastName.text()
    customer.address = wNewClient.inputAddress.text()
    customer.mobile = wNewClient.inputPhone.text()
    customer.email = wNewClient.inputEmail.text()
    customer.npaID = wNewClient.inputNPAId.cursorPosition()

    newRecord = (customer.firstname, customer.lastname, customer.address, customer.email, customer.mobile, customer.npaID)
    customer.createNew(newRecord)


def closeCurrentWindow():
    wNewClient.close()


def closeCurrentDetailsWindow():
    w_customer_details.close()


def refrechCustomerData():
    loadTableCustomers()
