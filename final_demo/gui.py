import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *
from stream import *


class Window(QtGui.QMainWindow):

    """This function is the init function for the GUI."""
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 400, 240)
        self.setWindowTitle("Live Sentiment Analysis")
        self.setWindowIcon(QtGui.QIcon('favicon.png'))
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Search Term")
        self.textbox.move(40, 50)
        self.textbox.resize(280, 40)
        self.label = QtGui.QLabel(self)
        self.label.move(40, 30)
        self.label.setText("Search Term:")
        self.textbox2 = QLineEdit(self)
        self.textbox2.setPlaceholderText("Number of Tweets to analyse")
        self.textbox2.move(40, 110)
        self.textbox2.resize(280, 40)
        self.label2 = QtGui.QLabel(self)
        self.label2.move(40, 90)
        self.label2.setText("Number of Tweets:")
        self.progressBar = QtGui.QProgressBar(self)
        self.progressBar.setGeometry(30, 40, 200, 25)

        runAction = QtGui.QAction("&Run", self)
        runAction.setShortcut("Return")
        runAction.setStatusTip('Run the Analyser')
        runAction.triggered.connect(self.on_click)

        quitAction = QtGui.QAction("&Quit", self)
        quitAction.setShortcut("Esc")
        quitAction.setStatusTip('Quit the Analyser')
        quitAction.triggered.connect(self.close_application)

        self.statusBar()
        self.statusBar().addPermanentWidget(self.progressBar)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(runAction)
        fileMenu.addAction(quitAction)


        self.home()

    """This function builds the buttons and adds them to the window."""
    def home(self):
        btn = QtGui.QPushButton("Analyse", self)
        btn.move(40, 170)
        btn.clicked.connect(self.start)
        btn2 = QtGui.QPushButton("Quit", self)
        btn2.move(200, 170)
        btn2.clicked.connect(self.close_application)
        self.show()
    """This function defines what happens when the run button is pressed."""
    def on_click(self):
        text = self.textbox.text()
        text2 = self.textbox2.text()
        if text == '':
            self.show_error()

        elif text2 == '':
            self.show_error()

        elif text2 != int:
            self.show_error()

        else:
            run(text, int(text2))
            self.show_results()
            self.progressBar.setRange(0, 1)
    """This function starts the progress bar."""
    def start(self):
        self.progressBar.setRange(0, 0)
        self.on_click()
    """This function closes the application"""
    def close_application(self):
        ask = QtGui.QMessageBox.question(self, "Quit", "Are you sure you want to quit?",
                                         QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if ask == QtGui.QMessageBox.Yes:
            print("Goodbye")
            sys.exit()
        else:
            pass
    """This function shows an error message if no input is detected in the window."""
    def show_error(self):
        ask = QtGui.QMessageBox.question(self, "Missing Search Data", "Please enter a search term and the required "
                                                                      "number of tweets to Analyse. \nPlease note that "
                                                                      "the number of tweets you wish to analyse must "
                                                                      "be a number. \n"
                                                                      "Do you "
                                                                      "wish to Continue?",
                                         QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if ask == QtGui.QMessageBox.No:
            print("Goodbye")
            sys.exit()
        else:
            pass

    """This window displays the results"""
    def show_results(self):
        results = QtGui.QMessageBox.question(self, "Results", ((str(final_results).strip('[]\'') + '\n' + '\n' +
                "The Most Common Adjectives in these tweets were:" + '\n' + '\n' + (str(final_count).strip('\"{][\'}'))
                                                            + '\n' + '\n' + "JJ = Adjective, JJS = Superlative "
                                                                            "Adjective and JJR = Comparative Adjective")
                                                               + '\n' + '\n' +
                                          "Do you wish to perform another search?"), QtGui.QMessageBox.Yes,
                                             QtGui.QMessageBox.No)
        if results == QtGui.QMessageBox.No:
            print("Goodbye")
            sys.exit()
        else:
            pass

"""This function starts the GUI"""
def start_gui():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


start_gui()
