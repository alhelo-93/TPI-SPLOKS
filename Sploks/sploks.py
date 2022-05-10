from PyQt5 import QtWidgets, uic
import sys
from controler import menuControler as Menu


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        Menu.displayMenu(self)  # Display the Mainmenu of Sploks
        self.setWindowTitle("Sploks")  # Set the window title to Sploks
        self.show()  # Display the app


# Create an instance of QtWidgets.QApplication
app = QtWidgets.QApplication(sys.argv)
# Create an instance of our class
window = Ui()
# Start the application
app.exec_()
