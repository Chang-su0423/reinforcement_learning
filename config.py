# 配置文件，存储强化学习的超参数和环境配置

# 环境参数
MAP_SIZE = 10  # 地图大小，10x10
OBSTACLE_RATIO = 0.2  # 障碍物的密度
# config.py
START_POSITION = (0, 0, 0)  # AUV起始位置 (x, y, z)
END_POSITION = (9, 9, 0)    # AUV目标位置 (x, y, z)


# 强化学习超参数
LEARNING_RATE = 0.001
GAMMA = 0.99  # 折扣因子
EPSILON = 0.1  # epsilon-greedy策略中的epsilon值
BATCH_SIZE = 32
EPISODES = 200
