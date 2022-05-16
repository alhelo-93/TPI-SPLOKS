from PyQt5 import QtWidgets, uic, QtCore
from model.staff import Staff


def displayStaffs():
    """
        * < displayCustomers >: Function that displays all the staffs
        * return: Returns nothing
    """
    global wStaffs
    wStaffs = uic.loadUi('views/staffs.ui')  # Load the .ui file

    global staff
    staff = Staff()
    ##
    wStaffs.tableStaff.cellClicked.connect(displayDetail)
    loadData()
    wStaffs.show()  # Show the window
    ##


def loadData():
    staffs = Staff.all()
    wStaffs.tableStaff.setColumnHidden(0, True)
    for row_number, staff in enumerate(staffs):
        wStaffs.tableStaff.insertRow(row_number)
        for column_number, data in enumerate(staff):
            cell = QtWidgets.QTableWidgetItem(str(data))
            wStaffs.tableStaff.setItem(row_number, column_number, cell)
            wStaffs.tableStaff.cellClicked.connect(loadStaffDetails)  ## get staff by his Id


def displayDetail():
    """
        * < displayDetail >: Function that displays the details of one staff using its id
        * return: Returns nothing
    """
    global w_staffs_details
    w_staffs_details = uic.loadUi('views/staffsDetails.ui')  # Load the .ui file
    w_staffs_details.btnSave.clicked.connect(updatePhoneNumber)
    w_staffs_details.btnSave.clicked.connect(refrechData)
    w_staffs_details.btnSave.clicked.connect(closeCurrentWindow)

    global staff_Id
    staff_Id = wStaffs.tableStaff.item(wStaffs.tableStaff.currentRow(), 0).text()
    staff.load(staff_Id)
    w_staffs_details.show()


def loadStaffDetails():
    """
        * < loadCustomerDetails >: Function that displays customer's details
        * return: Returns nothing
    """
    w_staffs_details.lblPrenom.setText(str(staff.firstname))  # Set label's text with firstname
    w_staffs_details.lblNom.setText(str(staff.lastname))  # Set label's text with the lastname
    w_staffs_details.inputphone.setText(str(staff.phone))  # Set label's text with phone


def updatePhoneNumber():
    value = w_staffs_details.inputphone.text()
    if not staff.update(value):
        print("test")


def closeCurrentWindow():
    w_staffs_details.close()


def refrechData():
    displayStaffs()
