class Point:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def draw(self):
        print(f"Point ({self.a} , {self.b})")
point=Point(1,2)
print(point.a)
point.draw()