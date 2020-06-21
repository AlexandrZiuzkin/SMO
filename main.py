###main.py – точка входа в программу

import sys  
from PyQt5 import QtWidgets
import design
from smo import *  

class ExampleApp(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)  
        
        self.SimulateBtn.clicked.connect(self.Calculate)
    
    def Calculate(self):
        
        labels_counter = [
        self.label000counter,
        self.label001counter,
        self.label100counter,
        self.label101counter,
        self.label011counter,
        self.label111counter,
        ]

        Ro = self.RoLineEdit
        P1 = self.P1LineEdit
        P2 = self.P2LineEdit
        Ticks = self.TicksLineEdit

        Acounter = self.Acounter
        Lccounter = self.Lccounter
        Wccounter = self.Wccounter
        Tickscounter = self.Tickscounter

        main_event(float(Ro.text()), float(P1.text()), float(P2.text()), int(Ticks.text()), labels_counter, Acounter, Lccounter, Wccounter, Tickscounter)
        

def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = ExampleApp()  
    window.show()  
    app.exec_()  

if __name__ == '__main__':  
    main()  