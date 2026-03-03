# main file

import sys 
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5.uic import loadUi
from gasCompressibilityFactor import zFactor


class MainWindow (QMainWindow): 
    def __init__(self): 
        super().__init__()
        
        loadUi ("mainUI.ui",self)
        self.calcBtn.clicked.connect(self.calcZ)
        
        
    def calcZ ( self ): 
        def safe_float(text):
            text = text.strip()
            text = text.replace(",", ".")
            
            if text == "":
                return 0.0
            
            try:
                return float(text)
            except ValueError:
                return 0.0
        
        try:
            pr = safe_float (self.PrInput.text())
            tr = safe_float (self.TrInput.text())
            z = zFactor(pr , tr)
            self.output_box.append(f"Ppr = {pr} ; Tpr = {tr}")
    
            self.output_box.append(f"z papayJ: {z.papayJ():.4f}")
            self.output_box.append(f"z Hall Yarbough: {z.hallYarbough():.4f}")
            self.output_box.append(f"z Dranchuk AbuKassem: {z.dranchukAbuKassem():.4f}")
            
    
            
    
            self.output_box.append("-----------------------------")
    
        except Exception as e:
            self.output_box.append(f"Error: {str(e)}")
            self.output_box.append("-----------------------------")

        
        
    
        
        



def window () : 
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


window()