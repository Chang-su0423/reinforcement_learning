import numpy as np
import random
from config import MAP_SIZE, OBSTACLE_RATIO, START_POSITION, END_POSITION

class AUVEnvironment:
    def __init__(self):
        self.map_size = MAP_SIZE
        self.obstacle_ratio = OBSTACLE_RATIO
        self.start_position = START_POSITION  # (x, y, z)
        self.end_position = END_POSITION      # (x, y, z)
        self.reset()

    def reset(self):
        # 重置环境
        self.map = np.zeros((self.map_size, self.map_size, self.map_size))  # 三维地图
        self.position = list(self.start_position)  # (x, y, z)
        self.steps = 0

        # 随机生成障碍物
        num_obstacles = int(self.map_size * self.map_size * self.map_size * self.obstacle_ratio)
        for _ in range(num_obstacles):
            x, y, z = np.random.randint(0, self.map_size, 3)  # 生成三维障碍物
            self.map[x, y, z] = 1  # 1代表障碍物
        self.map[self.position[0], self.position[1], self.position[2]] = 0  # 起点
        self.map[self.end_position[0], self.end_position[1], self.end_position[2]] = 0  # 终点
        return self.position  # 返回 (x, y, z)

    def step(self, action):
        # 执行动作并返回新的状态和奖励
        if action == 0:  # 上
            self.position[0] = max(0, self.position[0] - 1)
        elif action == 1:  # 下
            self.position[0] = min(self.map_size - 1, self.position[0] + 1)
        elif action == 2:  # 左
            self.position[1] = max(0, self.position[1] - 1)
        elif action == 3:  # 右
            self.position[1] = min(self.map_size - 1, self.position[1] + 1)
        elif action == 4:  # 向上（z方向）
            self.position[2] = max(0, self.position[2] - 1)
        elif action == 5:  # 向下（z方向）
            self.position[2] = min(self.map_size - 1, self.position[2] + 1)

        self.steps += 1

        # 判断是否碰到障碍物
        if self.map[self.position[0], self.position[1], self.position[2]] == 1:
            reward = -10  # 碰到障碍物惩罚
            done = True
        elif self.position == list(self.end_position):
            reward = 10  # 到达目标位置奖励
            done = True
        elif self.steps >= 200:  # 最大步数惩罚
            reward = -1
            done = True
        else:
            reward = -0.1  # 每一步移动都会有轻微惩罚，鼓励快速到达目标
            done = False

        return self.position, reward, done

