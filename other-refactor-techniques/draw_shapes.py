# by Kami Bigdely
# Extract superclass.
class Shape:
    def __init__(self, shape, x, y, width, visible=True, height=0):
        self.shape = shape
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = visible
    
    def display(self):
        if not self.visible:
            return -1
        if self.shape == 'rect':
            print('drew the rectangle')
        elif self.shape == 'circle':
            print('drew the circle')

    def hide(self):
        self.visible = False

    def set_visible(self):
        self.visible = True
    
    def get_center(self):
        if self.shape == 'rect':
            return self.x + self.width/2, \
               self.y + self.height/2 
        elif self.shape == 'circle':
            return self.x, self.y

if __name__ == "__main__":
    circle = Shape('circle',0,0,10, False)
    circle.set_visible()
    circle.display()
    print('center point',circle.get_center())

    rect = Shape('rect',10, 10, 20, True, 5)
    rect.hide()
    rect.display() # does not display because it's hidden.
    rect.set_visible()
    rect.display()
    print('center point',rect.get_center())