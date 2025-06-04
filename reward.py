# 设计奖励函数

def get_reward(position, map, end_position):
    if position == list(end_position):
        return 10  # 到达目标位置
    if map[position[0], position[1]] == 1:  # 碰到障碍物
        return -10
    return -0.1  # 每一步惩罚
