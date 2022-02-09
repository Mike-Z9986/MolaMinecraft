from turtle import position
from ursina import *

# 立方体的类
class TestCube(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3(45,45,45)
            
        )

# 按钮
class Test_button(Button):
	def __init__(self,scale = 0.1):
		super().__init__(
			parent = scene,
			model = 'cube',
			texture = 'brick',
			color = color.white,
			highlight_color = color.red,
			pressed_color = color.lime)

	def input(self,key):
		if self.hovered:
			if key == 'left mouse down':
				punch_sound.play()


# 更新帧
def update():
	if held_keys['a']:
		cube.x -= 1 * time.dt

'''#  2d图像WASD移动设置
def update():
    if held_keys['a']:
        test_square.x -= 4  * time.dt
    if held_keys['d']:
        test_square.x += 4  * time.dt
    if held_keys['w']:
        test_square.y += 4  * time.dt
    if held_keys['s']:
        test_square.y -= 4  * time.dt
'''

app = Ursina()

# 页面框
window.title = 'MolaMinecraft'              
window.borderless = False              
window.fullscreen = False             
window.exit_button.visible = False      
window.fps_counter.enabled = True       

cube = Entity(model='quad', color=color.orange, scale = (2,5), position = (5,1))

# 创建块
test = TestCube()

# 创建按钮
btn = Test_button()
punch_sound = Audio('assets/punch', loop=False, autoplay=False)

app.run()
