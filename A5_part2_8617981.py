#Assignment 5
#Part 2
#Rachel Harrison
#8617981

class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle():

    def __init__(self,bottomLeft,topRight,color):
        '''(Rectangle,Point,Point,String)->None'''
        self.topRight=topRight
        self.bottomLeft=bottomLeft
        self.color=color

    def __repr__(self):
        '''(Rectangle)->String'''
        return "Rectangle("+repr(self.bottomLeft)+","+repr(self.topRight)+","+repr(self.color)+")"

    def __str__(self):
        '''(Rectangle)->String'''
        return "I am a "+self.color+" rectangle with bottom left corner at ("+str(self.bottomLeft.get()[0])+","+str(self.bottomLeft.get()[1])+") and top right corner at ("+str(self.topRight.get()[0])+","+str(self.topRight.get()[1])+")."

    def __eq__(self,other):
        '''(Rectangle,Rectangle)->Boolean'''
        if(self.topRight==other.topRight and self.bottomLeft==other.bottomLeft and self.color==other.color):
            return True
        return False
        
    def get_bottom_left(self):
        '''(Rectangle)->Point'''
        return self.bottomLeft

    def get_top_right(self):
        '''(Rectangle)->Point'''
        return self.topRight

    def get_color(self):
        '''(Rectangle)->String'''
        return self.color

    def get_perimeter(self):
        '''(Rectangle)->Number'''
        length=(self.topRight.get()[0]-self.bottomLeft.get()[0])
        width=(self.topRight.get()[1]-self.bottomLeft.get()[1])
        return 2*(length+width)

    def get_area(self):
        '''(Rectangle)->Numbe)'''
        length=(self.topRight.get()[0]-self.bottomLeft.get()[0])
        width=(self.topRight.get()[1]-self.bottomLeft.get()[1])
        return length*width

    def reset_color(self,color):
        '''(Rectangle,String)->None'''
        self.color=color

    def move(self,dx,dy):
        '''(Rectangle,Number,Number)->None'''
        self.bottomLeft.move(dx,dy)
        self.topRight.move(dx,dy)

    def intersects(self,other):
        '''(Rectangle,Rectangle)->boolean'''
        if(self.bottomLeft.get()[0]>other.topRight.get()[0] or other.bottomLeft.get()[0]>self.topRight.get()[0]):
            return False
        if(self.bottomLeft.get()[1]>other.topRight.get()[1] or other.bottomLeft.get()[1]>self.topRight.get()[1]):
            return False
        return True

    def contains(self,x,y):
        '''(Rectangle,Number,Number)->boolean'''
        if(self.topRight.get()[0]>=x and x>=self.bottomLeft.get()[0] and self.topRight.get()[1]>=y and y>=self.bottomLeft.get()[1]):
            return True
        return False

class Canvas():

    def __init__(self):
        '''(Canvas)->None'''
        self.rectangles=[]

    def __len__(self):
        '''(Canvas)->int'''
        return len(self.rectangles)

    def __repr__(self):
        '''(Canvas)->String'''
        return "Canvas("+repr(self.rectangles)+")"

    def add_one_rectangle(self,rectangle):
        '''(Canvas,Rectangle)->None'''
        self.rectangles.append(rectangle)

    def count_same_color(self,color):
        '''(Cavas,String)->int'''
        counter=0
        for i in range(len(self.rectangles)):
            if self.rectangles[i].get_color()==color:
                counter+=1
        return counter

    def total_perimeter(self):
        '''(Canvas)->Number'''
        perimeter=0
        for i in range(len(self.rectangles)):
            perimeter+=self.rectangles[i].get_perimeter()
        return perimeter

    def min_enclosing_rectangle(self):
        '''(Canvas)->Rectangle'''
        maxX=self.rectangles[0].topRight.get()[0]
        minX=self.rectangles[0].bottomLeft.get()[0]
        maxY=self.rectangles[0].topRight.get()[1]
        minY=self.rectangles[0].bottomLeft.get()[1]
        for i in range(1,len(self.rectangles)):
            if(self.rectangles[i].topRight.get()[0]>maxX):
                maxX=self.rectangles[i].topRight.get()[0]
            if(self.rectangles[i].bottomLeft.get()[0]<minX):
                minX=self.rectangles[i].bottomLeft.get()[0]
            if(self.rectangles[i].topRight.get()[1]>maxY):
                maxY=self.rectangles[i].topRight.get()[1]
            if(self.rectangles[i].bottomLeft.get()[1]<minY):
                minY=self.rectangles[i].bottomLeft.get()[1]
        return Rectangle(Point(minX,minY),Point(maxX,maxY),"blue")

    def common_point(self):
        '''(Canvas)->boolean'''
        for i in range(len(self.rectangles)):
            for j in range(len(self.rectangles)):
                if(self.rectangles[i].intersects(self.rectangles[j])==False):
                    return False
        return True
                            
               
                       
