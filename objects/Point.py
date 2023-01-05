class Point:
    def __init__(self, point_t=(0, 0)):
        self.x = round(point_t[0])
        self.y = round(point_t[1])

    def move(self, x, y):
        self.x += x
        self.y += y

    def invert_y(self):
        self.y = -self.y

    def __tuple__(self):
        return (self.x, self.y)
