class Map:
    def __init__(self, size_x, size_y, empty_char = '_'):
        self.size_x = size_x
        self.size_y = size_y
        self.map = []
        self.empty_char = empty_char

        for y in range(self.size_y):
            self.map.append([])
            for x in range(self.size_x):
                self.map[y].append('_')

    def print(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                print(self.map[y][x], end='')
            print()

    def clean(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                self.map[y][x] = self.empty_char

    def setValue(self, x, y, char):
        self.map[y][x] = char
