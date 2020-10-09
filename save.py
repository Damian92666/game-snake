class Save:

    def save(self, apple, snake):
        content = []
        content.append(str(apple.x) + ';' + str(apple.y))
        for snake_point in snake.body:
            content.append(str(snake_point.x) + ';' + str(snake_point.y))
        with open('my_save.txt', 'w') as f:
            f.writelines(content)

    def load(self):
        content = []
        import os
        if os.path.exists('my_save.txt'):
            with open('my_save.txt', 'r') as f:
                content = f.readlines()
        else:
            print('plik nie istnieje')
        print(content)
