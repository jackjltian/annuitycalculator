#Jack JiaLiang Tian
#19.01.2016

import math

class Annuity(object):
    
    def __init__(self, pvav, leveled, arigeo, diff, 
                 variables):
        
        self.pvav = pvav     
        self.leveled = False
        self.arigeo = arigeo
        self.diff = diff
        self.variables = [0, 0, 0, 0, 0]

    def prompt(self):
        
        while 'x' not in self.variables:
            print ('========================================================')
            self.variables[0] = input('n = ')
            self.variables[1] = input('i/c = ')
            self.variables[2] = input('accumulate value. x if not available')
            self.variables[3] = input('payments = ')
            self.variables[4] = input('loan = ')
            
        self.pvav = input('"p" for present value, "a" for accumulate value.')
        #self.leveled = input('Are the payments constant? True or False.')
        #if self.leveled == 'False':
            #self.arigeo = input ('Is the annuity arithmetic or geometric?\
            #"a" or "g"')
            #self.diff = input('What is the difference factor?') 
    
    
    def main(self):
        self.prompt()
        if self.pvav == 'p':
            return PresentValue.solve(self)
        
        
    
class PresentValue(Annuity):
    
    def __init__(self, pvav, leveled, arigeo, diff, 
             variables):
        Annuity.__init__(self, pvav, leveled, arigeo, diff, 
             variables)
        
    def nearly_equal(a, b, sig_fig):
        return ( a==b or 
            int(a*10**sig_fig) == int(b*10**sig_fig)
                )       
    
    def solve(self):
        
        if self.variables[0] == 'x':
            return print(math.log(-(float(self.variables[3])/float(self.variables[4])) + 1)/math.log(1/(1+(float(self.variables[1])))))
        
        if self.variables[1] == 'x':
            a = float(self.variables[4])
            l = float(self.variables[3])
            n = float(self.variables[0])  
            s = float(self.variables[2])
            i0 = float(0.001)
            i1 = float(1)  
            midpoint = (i0 + i1)/2
            v = (1/(1+i0))**n
            p = (1 - v)/i0  
            return ((s/a)**(1/n) - (float(1)))

        if self.variables[3] == 'x':
            a = float(self.variables[4])
            n = float(self.variables[0])
            i = float(self.variables[1])
            v = (1/(1+i))**n
            p = (1 - v)/i
            return print(a/p)
        
        if self.variables[4] == 'x':
            n = float(self.variables[0])
            i = float(self.variables[1])
            l = float(self.variables[3])
            v = (1/(1+i))**n
            p = (1 - v)/i
            return print(l*p)

            
        
if __name__ == "__main__":
    
    n, i, c, p, l = 0, 0, 0, 0, 0
    variables = [n, i, c, p, l]
    pvav = 'a'     
    leveled = False
    arigeo = 'ari'
    diff = 0    
    tempannuityobject = Annuity(pvav, leveled, arigeo, diff, variables)
    tempannuityobject.main()