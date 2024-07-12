import random
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
        if X[i] - X[i-1] == 0:
            slope = 0
        else:
            slope = (Y[i] - Y[i-1]) / (X[i] - X[i-1])
        slopes.append(slope)
    return slopes


def find_start_end_pairs(X, slope_list, target_k):
    start_end_pairs = []
    start_index = None
    for i in range(len(slope_list)):
        if start_index is None:
            if slope_list[i] > target_k:
                start_index = i
        else:
            if slope_list[i] > (-1 * target_k) and slope_list[i] <= 0:
                end_index = i
                start_end_pairs.append((start_index, end_index))
                start_index = None
    return start_end_pairs

X = []
Y = []
for i in range(100):
    temp = random.randint(1,100)
    temp2 = random.randint(1,100)
    X.append(temp)
    Y.append(temp2)

slope_list = calculate_slope(X, Y)
temp = find_start_end_pairs(X, slope_list, 10)
# for item in temp:
#     print(slope_list[item[0]],slope_list[item[1]])
#     print(slope_list[item[0]-1],slope_list[item[1]-1])
# print(temp)
