from pico2d import *
import random

# Game object class here

class Grass:
    def __init__(self): #생성자 함수 : ppt 참고
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Small_ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599
        self.image = load_image('ball21x21.png')

    def update(self):
        self.y -= random.randint(1,50)
        if self.y <= 60:
            self.y = 60

    def draw(self):
        self.image.draw(self.x, self.y)
class Big_ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599
        self.image = load_image('ball41x41.png')

    def update(self):
        self.y -= random.randint(1,50)
        if self.y <= 75:
            self.y = 75


    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

# initialization code
def reset_world():
    global running
    global grass
    global team
    global big_balls
    global small_balls
    global world

    running = True
    world = []  # world list는 모든 객체들을 때려 넣은 것이다. 이를 이용하면 수정할 내용이 생겼을 떄 update_world나 render_world를 각각 수정하지 않아도 된다.

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(10)]
    world += team

    small_balls = [Small_ball() for i in range(10)]
    world += small_balls

    big_balls = [Big_ball() for i in range(10)]
    world += big_balls

def update_world():
    # grass.update()
    # for boy in team:
    #     boy.update()
    for o in world:
        o.update()

    pass

def render_world():
    clear_canvas()
    # grass.draw()
    # for boy in team:
    #     boy.draw()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
