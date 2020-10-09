from snake_snake import Point
from mapa_snake import Map
from snake_snake import Snake
from getkey import GetKey, ClearConsole, Wait
import random
from save import Save

if __name__ == '__main__':
    my_map = Map(10, 10, '-')
    my_snake = Snake(5, 5, 10, 10)
    my_apple = Point(random.randrange(10), random.randrange(10), 'A')

    game_over = False
    my_points = 0
    getKey = GetKey()
    my_save = Save()
    my_load = Save()

while True:
    ClearConsole()
    my_map.clean()

    key = getKey()
    if key == 27:
        my_save.save(my_apple, my_snake)
        my_load.load()
        break
    elif key == 301:
        my_snake.direction.x = 1
        my_snake.direction.y = 0
    elif key == 299:
        my_snake.direction.x = -1
        my_snake.direction.y = 0
    elif key == 296:
        my_snake.direction.x = 0
        my_snake.direction.y = -1
    elif key == 304:
        my_snake.direction.x = 0
        my_snake.direction.y = 1

    my_snake.move()

    for i in range(1, len(my_snake.body)):
        if my_snake.body[i].x == my_snake.body[0].x and my_snake.body[i].y == my_snake.body[0].y:
            game_over = True

    if game_over:
        print('!!!!!!!!!!!!!!!!!!!!! GAME OVER !!!!!!!!!!!!!!!!!!!!!')
        print('Click ESC to EXIT')
    if game_over:
        break

    my_map.setValue(my_apple.x, my_apple.y, my_apple.char)

    for point in my_snake.body:
        my_map.setValue(point.x, point.y, point.char)

    my_map.print()
    print('Points:', my_points)

    Wait()

    if my_snake.body[0].x == my_apple.x and my_snake.body[0].y == my_apple.y:
        my_snake.add_tail()
        my_apple = Point(random.randrange(10), random.randrange(10), 'A')
        my_points += 1
