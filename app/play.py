import pygame
import random
import sys

# Инициализация pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 800
CELL_SIZE = 20

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MEDIUMBLUE = (0, 0, 205)
DARKRED = (139, 0, 0)

# Создаем окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Змейка')

# Создаем часы для контроля FPS
clock = pygame.time.Clock()

# Шрифт для отображения счета
font = pygame.font.SysFont('Arial', 25)

def draw_rect(color, position):
    rect = pygame.Rect(position[0], position[1], CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)

def get_random_food_position():
    x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    return (x, y)

def main():
    snake_pos = [WIDTH // 2, HEIGHT // 2]
    snake_body = [list(snake_pos)]
    direction = 'RIGHT'
    change_to = direction

    food_pos = get_random_food_position()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Обработка нажатий клавиш
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        # Обновляем направление движения
        direction = change_to

        # Обновляем позицию змейки в зависимости от направления
        if direction == 'UP':
            snake_pos[1] -= CELL_SIZE
        elif direction == 'DOWN':
            snake_pos[1] += CELL_SIZE
        elif direction == 'LEFT':
            snake_pos[0] -= CELL_SIZE
        elif direction == 'RIGHT':
            snake_pos[0] += CELL_SIZE

        # Добавляем новую позицию в тело змейки
        snake_body.insert(0, list(snake_pos))

        # Проверка на съедание еды
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 10
            food_pos = get_random_food_position()
        else:
            # Удаляем хвост змейки если не съели еду
            snake_body.pop()

        # Проверка столкновений с границами или самим собой
        if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
            snake_pos[1] < 0 or snake_pos[1] >= HEIGHT):
            game_over(score)

        for block in snake_body[1:]:
            if block[0] == snake_pos[0] and block[1] == snake_pos[1]:
                game_over(score)

        # Отрисовка экрана
        screen.fill(BLACK)

        # Рисуем еду
        draw_rect(DARKRED, food_pos)

        # Рисуем змейку
        for pos in snake_body:
            draw_rect(MEDIUMBLUE, pos)

        # Отображение счета
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()

        clock.tick(8)  # Скорость игры

def game_over(score):
    font_game_over = pygame.font.SysFont('Arial', 50)
    game_over_surface = font_game_over.render('Game Over', True, DARKRED)
    score_surface = font.render(f'Score: {score}', True, WHITE)
    screen.blit(game_over_surface, ((WIDTH - game_over_surface.get_width()) //2,
                                    (HEIGHT - game_over_surface.get_height()) //2 -50))
    screen.blit(score_surface, ((WIDTH - score_surface.get_width()) //2,
                                (HEIGHT - score_surface.get_height()) //2 +10))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
