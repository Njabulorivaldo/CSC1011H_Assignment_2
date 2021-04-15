import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
    
class Game(QWidget): # MyWidget inherits from QWidget
    
    def __init__(self, parent=None): # parent defines parent widget
        QWidget.__init__(self, parent) # super class constructor
        self.setGeometry(250, 250, 250, 250) # x,y,width,height
        self.setWindowTitle('Guessing Game')
        self.grids()
         
    def close_button(self):
        #quits the game
        self.close()
        
    def new_game(self):
        '''
        Restarts the game when the user presses the new game button
        '''
        self.guess_1.setText('')
        self.guess_2.setText('')
        self.guess_3.setText('')
        
        self.first_guess.setText('')
        self.sec_guess.setText('')
        self.third_guess.setText('')
        
        self.dis1.setText('')        
        self.dis2.setText('')     
        self.dis3.setText('')     
        #new random number
        self.number = random.randint(1,10)
        
    def text(self):
        #holds the guess number entered by the user
        self.edit.text()
     
    def clicked(self):
        '''
        esponsible for the change of the color and picture on the game!!!
        '''
        if self.color_combo.currentText() == 'red':     #red background
            self.setAutoFillBackground(True)
            bg_color = self.palette()
            bg_color.setColor(self.backgroundRole(), Qt.red)
            self.setPalette(bg_color)
        else:
            self.setAutoFillBackground(True)    #blue background
            bg_color = self.palette()
            bg_color.setColor(self.backgroundRole(), Qt.blue)
            self.setPalette(bg_color)
        
        if self.pic_combo.currentText() == 'mickey':    #mickey picture widget
            self.pic.setPixmap(QPixmap('mickey.gif'))
        else:
            self.pic.setPixmap(QPixmap('pluto.gif'))    #pluto picture widget
                  
    def guesses(self):
        '''
        Shows the guess number, number guessed and whether it is correct or not then provide a hint
        '''
        while True:
            if self.guess_1.text() == '' :
                self.guess_1.setText('Guess 1:')
                if int(self.edit.text()) == self.number:
                    self.first_guess.setText(self.edit.text())
                    self.dis1.setText('Correct!')
                elif int(self.edit.text()) < self.number:
                    self.first_guess.setText(self.edit.text())
                    self.dis1.setText('Too small')
                else:
                    self.first_guess.setText(self.edit.text())
                    self.dis1.setText('Too big')
                break
            
            elif self.guess_2.text() == '':
                self.guess_2.setText('Guess 2:')
                if int(self.edit.text()) == self.number:
                    self.sec_guess.setText(self.edit.text())
                    self.dis2.setText('Correct!')
                elif int(self.edit.text()) < self.number:
                    self.sec_guess.setText(self.edit.text())
                    self.dis2.setText('Too small')
                else:
                    self.sec_guess.setText(self.edit.text())
                    self.dis2.setText('Too big')
                break
            
            elif self.guess_3.text() == '':
                self.guess_3.setText('Guess 3:') 
                if int(self.edit.text()) == self.number:
                    self.third_guess.setText(self.edit.text())
                    self.dis3.setText('Correct!')
                elif int(self.edit.text()) < self.number:
                    self.third_guess.setText(self.edit.text())
                    self.dis3.setText('Too small')   
                else:
                    self.third_guess.setText(self.edit.text())
                    self.dis3.setText('Too big') 
                break            
            break    
        
    def grids(self):
        '''
        Adds all the widgets into the window in grids
        '''
        grid = QGridLayout()#creates grid layout
        
        #creates an initial background color
        self.setAutoFillBackground(True)
        bg_color = self.palette()
        bg_color.setColor(self.backgroundRole(), Qt.red)
        self.setPalette(bg_color)
        
        #creates an initial display image
        self.pic = QLabel(self)
        pixmap = QPixmap('mickey.gif')
        self.pic.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        grid.addWidget(self.pic, 0,0,15,1)
        
        #guess displays
        guess = QLabel('Guesses:')
        guess.setFont(QFont('Bold',15,2))
        grid.addWidget(guess, 0,1)
        
        #shows nothing initially until the user make guesses
        self.guess_1 = QLabel('')
        self.guess_2 = QLabel('')
        self.guess_3 = QLabel('')
        grid.addWidget(self.guess_1,1,1)
        grid.addWidget(self.guess_2,2,1)
        grid.addWidget(self.guess_3,3,1)   
        
        self.first_guess = QLabel('')
        self.sec_guess = QLabel('')
        self.third_guess = QLabel('')
        grid.addWidget(self.first_guess,1,2)
        grid.addWidget(self.sec_guess,2,2)
        grid.addWidget(self.third_guess,3,2)
        
        self.dis1 = QLabel('')
        self.dis2 = QLabel('')
        self.dis3 = QLabel('')
        grid.addWidget(self.dis1, 1,3)
        grid.addWidget(self.dis2, 2,3)
        grid.addWidget(self.dis3, 3,3)
        
        #user edit entry
        self.edit = QLineEdit(self)
        grid.addWidget(self.edit,4,2)        
        
        #random number
        self.number = random.randint(1,10)
        
        self.guess_button = QPushButton('Guess')
        self.guess_button.clicked.connect(self.text)                                         # +++
        self.guess_button.clicked.connect(self.guesses)                                         # +++
        grid.addWidget(self.guess_button, 4,3)        
        
        #Interface controls
        inter = QLabel('Interface:') 
        inter.setFont(QFont('Bold',15,2))#heading formatting
        grid.addWidget(inter, 7,1)        
        
        pic = QLabel('Picture:')
        color = QLabel('Colour:')
        grid.addWidget(pic, 8,1)
        grid.addWidget(color, 9,1)        
        
        self.closer = QPushButton('Close')
        self.closer.clicked.connect(self.close_button)                                     # +++
        grid.addWidget(self.closer, 10, 1)         
        
        self.change = QPushButton('Change')
        grid.addWidget(self.change, 9,3)        
        self.change.clicked.connect(self.clicked)    
        
        self.new = QPushButton('New Game')
        self.new.clicked.connect(self.new_game)   
        grid.addWidget(self.new, 10,2)
        
        self.color_combo = QComboBox()
        self.color_combo.addItem('red')
        self.color_combo.addItem('blue')      
        grid.addWidget(self.color_combo,9,2)
        
        self.pic_combo = QComboBox()
        self.pic_combo.addItem('mickey')
        self.pic_combo.addItem('pluto')
        grid.addWidget(self.pic_combo,8,2)
         
        self.setLayout(grid)
    
if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        window = Game() # create MyWidget object
        window.show()
        sys.exit(app.exec_())
    except:
        pass