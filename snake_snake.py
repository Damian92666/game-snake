from punkt_snake import Point


class Snake:

    def __init__(self, x, y, size_x, size_y):
        self.body = [Point(x, y, 'X')]
        self.direction = Point(1, 0, '')
        self.size_x = size_x
        self.size_y = size_y

    def move(self):
        for i in reversed(range(1, len(self.body))):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.direction.x
        self.body[0].y += self.direction.y

        if self.body[0].x >= self.size_x:
            self.body[0].x = 0
        elif self.body[0].x < 0:
            self.body[0].x = self.size_x - 1

        if self.body[0].y >= self.size_y:
            self.body[0].y = 0
        elif self.body[0].y < 0:
            self.body[0].y = self.size_y - 1

    def add_tail(self):
        self.body.append(Point(self.body[0].x, self.body[0].y, 'X'))
