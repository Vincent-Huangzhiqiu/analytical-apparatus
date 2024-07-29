import matplotlib.pyplot as plt
import decimal
from utils import get_relative_time, read_file, calculate_slope, find_start_end_pairs
target_machine = "SDPR1"
interval = 0.2  # 每个时间点的间隔为200毫秒
file_path = 'data.txt'

def get_X_and_Y(file_path, target_machine, interval):
    # 获得绘图时的X和Y轴数据
    raw_data = read_file(file_path)
    data = []
    for item in raw_data:
        if "RxD" in item and target_machine in item:
            data.append(item)
    machine_time = []
    unprocessed_Y = []
    for item in data:
        temp_x, temp_y = item.split(target_machine)
        machine_time.append(temp_x.split(" ")[0])
        y = temp_y.replace(" ", "")
        unprocessed_Y.append(y.strip())
    machine_time = get_relative_time(machine_time)

    X = []
    start_time = 0
    len_X = len(machine_time) * int(1 / interval)
    for x in range(len_X):
        X.append(start_time + x * interval)
    temp = [decimal.Decimal(i).quantize(decimal.Decimal('0.001')) for i in X]
    X = temp

    Y = []
    for y in unprocessed_Y:
        temp = y.split(",")
        for item in temp:
            Y.append(int(item))
    return X, Y


if __name__ == "__main__":
    X, Y = get_X_and_Y(file_path, target_machine, interval)
    slope_list = calculate_slope(X, Y)
    start_end_pairs = find_start_end_pairs(X, slope_list, 10)
    for item in start_end_pairs:
        print(slope_list[item[0]],slope_list[item[1]])
        print(slope_list[item[0]-1],slope_list[item[1]-1])
    print(start_end_pairs)
    plt.scatter(X, Y, color='blue', label='Data Points')
    plt.title('Scatter Plot of Generated Data Points')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.show()