import numpy as np
import random
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from config import GAMMA, EPSILON, BATCH_SIZE, LEARNING_RATE, EPISODES

from keras.optimizers import Adam

class DQNAgent:
    def __init__(self, action_space):
        self.action_space = action_space
        self.memory = deque(maxlen=2000)
        self.model = self._build_model()
        self.epsilon = EPSILON  # epsilon-greedy策略中的epsilon值

    def _build_model(self):
        model = Sequential()
        model.add(Dense(24, input_dim=3, activation='relu'))  # 输入为AUV的位置 (x, y, z)
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_space, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(learning_rate=LEARNING_RATE))  # 修改为learning_rate
        return model

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.choice(range(self.action_space))  # 随机选择动作
        q_values = self.model.predict(np.array([state]))
        return np.argmax(q_values[0])  # 选择Q值最大的动作

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def replay(self):
        if len(self.memory) < BATCH_SIZE:
            return
        minibatch = random.sample(self.memory, BATCH_SIZE)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = reward + GAMMA * np.amax(self.model.predict(np.array([next_state]))[0])
            target_f = self.model.predict(np.array([state]))
            target_f[0][action] = target
            self.model.fit(np.array([state]), target_f, epochs=1, verbose=0)
