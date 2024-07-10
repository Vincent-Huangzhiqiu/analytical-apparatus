import matplotlib.pyplot as plt

target_machine = "SDPR1"
interval = 200  # 每个时间点的间隔为200毫秒

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
    return content

def time_to_milliseconds(time_str):
    # 将时间字符串转换为时间戳（以毫秒为单位）
    h, m, s = map(float, time_str.split(':'))
    ms = int(h * 3600000 + m * 60000 + s * 1000)
    return ms

def get_relative_time(time_list):
    # 计算相对时间（从0开始）
    timestamps = [time_to_milliseconds(t) for t in time_list]
    start_time = timestamps[0]
    relative_times = [t - start_time for t in timestamps]   
    return relative_times

def get_X_and_Y(target_machine, interval):
    # 获得绘图时的X和Y轴数据
    file_path = 'data.txt'
    raw_data = read_file(file_path)
    data = []
    for item in raw_data:
        if "RxD" in item and target_machine in item:
            data.append(item)
    unprocessed_X = []
    unprocessed_Y = []
    for item in data:
        temp_x, temp_y = item.split(target_machine)
        unprocessed_X.append(temp_x.split(" ")[0])

        y = temp_y.replace(" ", "")
        unprocessed_Y.append(y.strip())
    
    processed_X = get_relative_time(unprocessed_X)

    X = []
    for x in processed_X:
        for i in range(5):
            X.append(x + i * interval)

    Y = []
    for y in unprocessed_Y:
        temp = y.split(",")
        for item in temp:
            Y.append(item)

    return X, Y


if __name__ == "__main__":
    X, Y = get_X_and_Y(target_machine, interval)

    plt.scatter(X, Y, color='blue', label='Data Points')
    plt.title('Scatter Plot of Generated Data Points')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.show()