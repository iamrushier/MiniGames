global position
position=0       

class L:
    coordinates=[(4,1),(1,2),(2,2),(3,2),(4,2)]
    def __init__(self):
         self.coordinates=[(4,1),(1,2),(2,2),(3,2),(4,2)]  
    def position_0(self,x,y):
        self.coordinates=[ (x+1,y-1), (x-2,y), (x-1,y), (x,y), (x+1,y) ]
        u,v=x,y
    def position_1(self,x,y):
        self.coordinates=[ (x+1,y+1), (x,y-2), (x,y-1), (x,y), (x,y+1) ]
    def position_2(self,x,y):
        self.coordinates=[ (x-2,y-1), (x+1,y), (x,y), (x-1,y), (x-2,y) ]
    def position_3(self,x,y):
        self.coordinates=[ (x-1,y-2), (x,y+1), (x,y), (x,y-1), (x,y-2) ]

        
class J:
    coordinates=[(0,1),(0,2),(1,2),(2,2),(3,2)]
    def __init__(self):
        self.coordinates=[(0,1),(0,2),(1,2),(2,2),(3,2)]
         
    def position_0(self,x,y):
        self.coordinates=[ (x-2,y-1), (x-2,y), (x-1,y), (x,y), (x+1,y) ]
        u,v=x,y
        
    def position_1(self,x,y):
        self.coordinates=[ (x+1,y-2), (x,y-2), (x,y-1), (x,y), (x,y+1) ]
        
    def position_2(self,x,y):
        self.coordinates=[ (x+1,y-1), (x+1,y), (x,y), (x-1,y), (x-2,y) ]
        
    def position_3(self,x,y):
        self.coordinates=[ (x-1,y+1), (x,y+1), (x,y), (x,y-1), (x,y-2) ]
    
class Z:
    coordinates=[(1,1),(2,1),(2,2),(3,2)]
    def __init__(self):
         self.coordinates=[(1,1),(2,1),(2,2),(3,2)]
         
    def position_0(self,x,y):
        self.coordinates=[ (x-1,y-1), (x,y-1), (x,y), (x+1,y)]
        u,v=x,y
        
    def position_1(self,x,y):
        self.coordinates=[ (x+1,y-1), (x+1,y), (x,y), (x,y+1) ]
        
    def position_2(self,x,y):
        self.coordinates=[ (x+1,y), (x,y), (x,y-1), (x-1,y-1) ]
        
    def position_3(self,x,y):
        self.coordinates=[ (x,y+1), (x,y), (x+1,y), (x+1,y-1) ]
    
    
class T:
    coordinates=[(2,1),(1,2),(2,2),(3,2)]
    def __init__(self):
         self.coordinates=[(2,1),(1,2),(2,2),(3,2)]
         
    def position_0(self,x,y):
        self.coordinates=[ (x,y-1), (x-1,y), (x,y), (x+1,y) ]
        u,v=x,y
        
    def position_1(self,x,y):
        self.coordinates=[ (x+1,y),(x,y-1), (x,y), (x,y+1) ]
        
    def position_2(self,x,y):
        self.coordinates=[ (x,y+1), (x+1,y), (x,y), (x-1,y) ]
        
    def position_3(self,x,y):
        self.coordinates=[ (x-1,y), (x,y+1), (x,y), (x,y-1) ]
    
    
class O:
    coordinates=[(2,1),(3,1),(2,2),(3,2)]
    def __init__(self):
         self.coordinates=[(2,1),(3,1),(2,2),(3,2)]
         
    def position_0(self,x,y):
        self.coordinates=[ (x,y-1), (x+1,y-1), (x,y), (x+1,y) ]
        u,v=x,y
        
    def position_1(self,x,y):
        self.coordinates=[ (x+1,y-1), (x+1,y), (x,y-1), (x,y)]
        
    def position_2(self,x,y):
        self.coordinates=[ (x+1,y), (x,y), (x+1,y-1), (x,y-1)]
        
    def position_3(self,x,y):
        self.coordinates=[ (x,y), (x,y-1), (x+1,y), (x+1,y-1) ]
    
    
class S:
    coordinates=[(2,1),(3,1),(1,2),(2,2)]
    def __init__(self):
         self.coordinates=[(2,1),(3,1),(1,2),(2,2)]
         
    def position_0(self,x,y):
        self.coordinates=[ (x,y-1), (x+1,y-1), (x-1,y), (x,y) ]
        u,v=x,y
        
    def position_1(self,x,y):
        self.coordinates=[ (x+1,y), (x+1,y+1), (x,y-1), (x,y)]
        
    def position_2(self,x,y):
        self.coordinates=[ (x,y), (x-1,y), (x+1,y-1), (x,y-1)]
        
    def position_3(self,x,y):
        self.coordinates=[ (x,y), (x,y-1), (x+1,y+1), (x+1,y)]
    
    
class I:
    coordinates=[(0,2),(1,2),(2,2),(3,2)]
    def __init__(self):
         self.coordinates=[(0,2),(1,2),(2,2),(3,2)]
         
    def position_0(self,x,y):
        self.coordinates=[ (x-2,y), (x-1,y), (x,y), (x+1,y) ]
        u,v=x,y
        
    def position_1(self,x,y):
        self.coordinates=[ (x,y-2), (x,y-1), (x,y), (x,y+1) ]
        
    def position_2(self,x,y):
        self.coordinates=[ (x+1,y), (x,y), (x-1,y), (x-2,y) ]
        
    def position_3(self,x,y):
        self.coordinates=[ (x,y+1), (x,y), (x,y-1), (x,y-2) ]
    
    

