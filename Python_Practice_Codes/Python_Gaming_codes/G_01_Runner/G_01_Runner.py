import os
from sys import exit
from random import randint, choice

import pygame

# ---------------------------------------------------------------- 路径
BASE = os.path.dirname(os.path.abspath(__file__))


def img(rel_path, alpha=True):
    surface = pygame.image.load(os.path.join(BASE, rel_path))
    return surface.convert_alpha() if alpha else surface


def asset(*parts):
    return os.path.join(BASE, *parts)


# ---------------------------------------------------------------- 玩家
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_walk = [
            img('graphics/Player/player_walk_1.png'),
            img('graphics/Player/player_walk_2.png'),
        ]
        self.player_index = 0
        self.player_jump = img('graphics/Player/jump.png')

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0
        self.max_jumps = 2
        self.jumps_left = self.max_jumps

        self.jump_sound = pygame.mixer.Sound(asset('audio', 'jump.mp3'))
        self.jump_sound.set_volume(0.5)

    def jump(self):
        if self.jumps_left > 0:
            if self.jumps_left == self.max_jumps:
                self.gravity = -20
            else:
                self.gravity = -14
            self.jumps_left -= 1
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            self.gravity = 0
            self.jumps_left = self.max_jumps

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.apply_gravity()
        self.animation_state()

    def reset(self):
        self.rect.midbottom = (80, 300)
        self.gravity = 0
        self.jumps_left = self.max_jumps
        self.player_index = 0
        self.image = self.player_walk[0]


# ---------------------------------------------------------------- 障碍
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, kind):
        super().__init__()

        if kind == 'fly':
            self.frames = FLY_FRAMES
            y_pos = 210
        else:
            self.frames = SNAIL_FRAMES
            y_pos = 300

        self.speed = 12 if kind == "fly" else 5

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(800, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= self.speed
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


# ---------------------------------------------------------------- 初始化
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

test_font = pygame.font.Font(asset('font', 'Pixeltype.ttf'), 50)

game_active = False
start_time = 0
score = 0

FLY_FRAMES = [img('graphics/Fly/Fly1.png'), img('graphics/Fly/Fly2.png')]
SNAIL_FRAMES = [img('graphics/snail/snail1.png'), img('graphics/snail/snail2.png')]

sky_surface = img('graphics/Sky.png', alpha=False)
ground_surface = img('graphics/Ground.png', alpha=False)

pygame.mixer.music.load(asset('audio', 'music.wav'))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops=-1)

player = pygame.sprite.GroupSingle(Player())
obstacle_group = pygame.sprite.Group()

player_stand = pygame.transform.rotozoom(img('graphics/Player/player_stand.png'), 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render('Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 330))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)


# ---------------------------------------------------------------- 工具函数
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    return True


# ---------------------------------------------------------------- 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.sprite.jump()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                score = 0
                start_time = int(pygame.time.get_ticks() // 1000)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        player.sprite.reset()

        screen.blit(game_name, game_name_rect)
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
            score_message_rect = score_message.get_rect(center=(400, 330))
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)