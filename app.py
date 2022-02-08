from turtle import position
from ursina import *

# 立方体的类
class TestCube(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3(45,45,45)
            
        )

#  2d图像WASD移动设置
def update():
    if held_keys['a']:
        test_square.x -= 4  * time.dt
    if held_keys['d']:
        test_square.x += 4  * time.dt
    if held_keys['w']:
        test_square.y += 4  * time.dt
    if held_keys['s']:
        test_square.y -= 4  * time.dt


app = Ursina()

test_square = Entity(model = 'quad', color = color.red, scale=(1,4),position=None)

# sans_texture = load_texture('assets/Sans.png')
# sans = Entity(modle='circle', texture=sans_texture)
sans = Entity(modle='circle', texture='assets/Sans.png')

testcube = TestCube()

app.run()
