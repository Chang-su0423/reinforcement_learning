import numpy as np
from environment import AUVEnvironment
from agent import DQNAgent
from config import EPISODES
from utils import plot_path  # 导入plot_path函数
from config import MAP_SIZE  # 导入MAP_SIZE


def train():
    env = AUVEnvironment()
    agent = DQNAgent(action_space=4)

    for e in range(EPISODES):
        state = env.reset()
        done = False
        total_reward = 0
        steps = 0  # 记录每轮的步数
        path = [tuple(state)]  # 记录路径

        while not done:
            action = agent.act(state)
            next_state, reward, done = env.step(action)
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            path.append(tuple(state))  # 记录路径
            total_reward += reward
            steps += 1

        # 一轮结束，输出当前轮的信息
        print(f"Episode {e+1}/{EPISODES} - Total Reward: {total_reward} - Steps: {steps}")
          # 绘制路径

        if e % 10 == 0:  # 每50轮输出一次信息
            print(f"Episode {e+1} completed.")
            plot_path(path, MAP_SIZE, e)



if __name__ == "__main__":
    train()
