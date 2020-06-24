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

        ro = self.RoLineEdit
        p1 = self.P1LineEdit
        p2 = self.P2LineEdit
        ticks = self.TicksLineEdit

        ac_counter = self.Acounter
        lc_counter = self.Lccounter
        wc_counter = self.Wccounter
        ticks_counter = self.Tickscounter

        main_event(float(ro.text()), float(p1.text()), float(p2.text()), int(ticks.text()), labels_counter, ac_counter, lc_counter, wc_counter, ticks_counter)
        

def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = ExampleApp()  
    window.show()  
    app.exec_()  

if __name__ == '__main__':  
    main()  
