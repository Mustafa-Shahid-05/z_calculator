import numpy as np
from scipy.optimize import newton

class zFactor :
    def __init__(self , ppr , tpr):
        self.ppr = ppr 
        self.tpr = tpr 
    def papayJ (self):
        a = 3.53
        b = 0.9813
        c = 0.274
        d = 0.8157
        z = 1 - (a*self.ppr / (10**(b*self.tpr))) + ((c*self.ppr**2)/(10**(d*self.tpr)))
        return z
    def hallYarbough(self):
        t = 1 / self.tpr
        ppr = self.ppr

        X1 = -0.06125 * t * ppr * np.exp(-1.2 * (1 - t**2))
        X2 = 14.76 * t - 9.76 * t**2 + 4.58 * t**3
        X3 = 90.7 * t - 242.2 * t**2 + 42.4 * t**3
        X4 = 2.18 + 2.82 * t

        def F(Y):
            return X1 + (Y + Y**2 + Y**3 - Y**4) / (1 - Y)**3 - X2 * Y**2 + X3 * Y**X4

        def Fprime(Y):
            
            term1 = (1 + 4*Y + 4*Y**2 - 4*Y**3 + Y**4) / (1 - Y)**4
            term2 = -2 * X2 * Y
            term3 = X3 * X4 * Y**(X4 - 1)
            return term1 + term2 + term3

        Y0 = 0.0125 * ppr * t * np.exp(-1.2 * (1 - t**2))
        Y = newton(F, x0=Y0, fprime=Fprime)
        z = -X1 / Y
        return z
    def dranchukAbuKassem (self):
        ppr = self.ppr
        tpr = self.tpr
        A1 = 0.3262
        A2 = -1.0700
        A3 = -0.5339
        A4 = 0.01569
        A5 = -0.05165
        A6 = 0.5475
        A7 = -0.7361
        A8 = 0.1884
        A9 = 0.1056
        A10 = 0.6134
        A11 = 0.7210
        
        def f(rho):
            term1 = A1 + A2/tpr + A3/(tpr**2) + A4/(tpr**4) + A5/(tpr**5)
            term2 = A6 + A7/tpr + A8/(tpr**2)
            term3 = A9 * (A7/tpr + A8/(tpr**2))
            return term1*rho + term2*(rho**2) - term3*(rho**5)+A10 * (1 + A11*(rho**2)) * (((rho**2)*np.exp(A11 * (rho**2)))/(tpr**3)) + 1 - (0.27*ppr)/(rho*tpr) 
        rho_0 = (0.27*ppr)/tpr
        rho_r = newton(f, x0 = rho_0)
        z = (0.27*ppr)/(rho_r*tpr)
        return z
    
        
        
        
        
'''       
  
z = zFactor (ppr = 5 , tpr = 3)
zPapay = z.papayJ()
zHall = z.hallYarbough()
zDak = z.dranchukAbuKassem()

print (f"papay = {zPapay:.4f} , hall = {zHall:.4f} , dranchuk = {zDak:.4f}")  
      
'''          
        
            
        
            
            
            
            
            
            
      
    
        
    
