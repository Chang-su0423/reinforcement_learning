import matplotlib
matplotlib.use('TkAgg')  # 更改后端为 'TkAgg'
import matplotlib.pyplot as plt


def plot_path(path, map_size, episode):
    """
    绘制AUV的三维路径图。
    path: 记录路径的列表，存储每一步AUV的位置 (x, y, z)。
    map_size: 地图的大小。
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 分别提取路径的x, y, z坐标
    x = [pos[0] for pos in path]
    y = [pos[1] for pos in path]
    z = [pos[2] for pos in path]

    # 绘制路径
    ax.plot(x, y, z, color='r', marker='o', markersize=5)

    # 设置标签
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'AUV Path in 3D - Episode {episode}')

    # 保存图像
    plt.savefig(f'path_episode_{episode}.png')
    # 显示图像并设置暂停时间（例如3秒后自动关闭）
    plt.show(block=False)  # 非阻塞显示
    plt.pause(3)  # 3秒后自动关闭
    plt.close()  # 关闭图像窗口


