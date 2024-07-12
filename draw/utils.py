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

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
    return content

def calculate_slope(X, Y):
    # 计算斜率k
    slopes = []
    if len(X) != len(Y):
        raise ValueError("X和Y列表长度不一致")
    
    for i in range(1, len(X)):
        slope = (Y[i] - Y[i-1]) / (X[i] - X[i-1])
        slopes.append(slope)
    return slopes

# Example usage:
X = [1, 2, 3, 4, 5]
Y = [2, 4, 6, 8, 10]

slope_list = calculate_slope(X, Y)
print("Slope list:", slope_list)
