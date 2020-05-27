import sys
import pygame
from PyQt5 import QtCore, QtWidgets
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')


class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

    def display(self, screen, param):
        pass

class Ui_FirstWindow(object):
    def setupUi(self, FirstWindow):
        FirstWindow.setObjectName("FirstWindow")
        FirstWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(FirstWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 130, 191, 23))
        self.pushButton.setObjectName("pushButton")
        FirstWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(FirstWindow)
        QtCore.QMetaObject.connectSlotsByName(FirstWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("FirstWindow", "FirstWindow"))
        self.pushButton.setText(_translate("FirstWindow", "LoadSecondWindow"))

    def LoadSecondWindow(self):
        SecondWindow = QtWidgets.QMainWindow()
        ui = Ui_SecondWindow()
        ui.setupUi(SecondWindow)
        SecondWindow.show()

    class TextPrint(object):
        def __init__(self):
            self.reset()
            self.font = pygame.font.Font(None, 20)

        def tprint(self, screen, textString):
            textBitmap = self.font.render(textString, True, BLACK)
            screen.blit(textBitmap, (self.x, self.y))
            self.y += self.line_height

        def reset(self):
            self.x = 10
            self.y = 10
            self.line_height = 15

        def indent(self):
            self.x += 10

        def unindent(self):
            self.x -= 10

        def display(self, screen, param):
            pass
class Ui_SecondWindow(object):


    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(SecondWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 130, 191, 23))
        self.pushButton.setObjectName("pushButton")
        SecondWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

        pygame.init()
        done = False
        SecondWindow = pygame.display.set_mode((500, 700))
        pygame.display.set_caption("My Game")

        # Used to manage how fast the screen updates.
        clock = pygame.time.Clock()

        # Initialize the joysticks.
        pygame.joystick.init()

        # Get ready to print.
        textPrint = TextPrint()

        while not done:
            #
            # EVENT PROCESSING STEP
            #
            # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
            # JOYBUTTONUP, JOYHATMOTION
            for event in pygame.event.get():  # User did something.
                if event.type == pygame.QUIT:  # If user clicked close.
                    done = True  # Flag that we are done so we exit this loop.
                elif event.type == pygame.JOYBUTTONDOWN:
                    print("Joystick button pressed.")
                elif event.type == pygame.JOYBUTTONUP:
                    print("Joystick button released.")

            #
            # DRAWING STEP
            #
            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
            textPrint.reset()
            SecondWindow.fill(WHITE)

            # Get count of joysticks.
            joystick_count = pygame.joystick.get_count()

            textPrint.tprint(SecondWindow, "Number of joysticks: {}".format(joystick_count))
            textPrint.indent()

            # For each joystick:
            for i in range(joystick_count):
                joystick = pygame.joystick.Joystick(i)
                joystick.init()

                textPrint.tprint(SecondWindow, "Joystick {}".format(i))
                textPrint.indent()

                # Get the name from the OS for the controller/joystick.
                name = joystick.get_name()
                textPrint.tprint(SecondWindow, "Joystick name: {}".format(name))

                # Usually axis run in pairs, up/down for one, and left/right for
                # the other.
                axes = joystick.get_numaxes()
                textPrint.tprint(SecondWindow, "Number of axes: {}".format(axes))
                textPrint.indent()

                for i in range(axes):
                    axis = joystick.get_axis(i)
                    textPrint.tprint(SecondWindow, "Axis {} value: {:>6.3f}".format(i, axis))
                textPrint.unindent()

                buttons = joystick.get_numbuttons()
                textPrint.tprint(SecondWindow, "Number of buttons: {}".format(buttons))
                textPrint.indent()

                for i in range(buttons):
                    button = joystick.get_button(i)
                    textPrint.tprint(SecondWindow,
                                     "Button {:>2} value: {}".format(i, button))
                textPrint.unindent()

                hats = joystick.get_numhats()
                textPrint.tprint(SecondWindow, "Number of hats: {}".format(hats))
                textPrint.indent()

                # Hat position. All or nothing for direction, not a float like
                # get_axis(). Position is a tuple of int values (x, y).
                for i in range(hats):
                    hat = joystick.get_hat(i)
                    textPrint.tprint(SecondWindow, "Hat {} value: {}".format(i, str(hat)))
                textPrint.unindent()

            #
            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
            #

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # Limit to 20 frames per second.
            clock.tick(50)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("SecondWindow", "SecondWindow"))
        self.pushButton.setText(_translate("SecondWindow", "Congratz !"))


class Controller:

    def __init__(self):
        pass

    def Show_FirstWindow(self):
        self.FirstWindow = QtWidgets.QMainWindow()
        self.ui = Ui_FirstWindow()
        self.ui.setupUi(self.FirstWindow)
        self.ui.pushButton.clicked.connect(self.Show_SecondWindow)

        self.FirstWindow.show()

    def Show_SecondWindow(self):
        self.SecondWindow = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.SecondWindow)
        self.ui.pushButton.clicked.connect(self.Print)

        self.SecondWindow.show()

    def Print(self):
        print('After 99 hours of trying out everything')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()
    Controller.Show_FirstWindow()
    sys.exit(app.exec_())
