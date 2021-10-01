import csv

def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)

        next(reader)
        for line in reader:
            new_line = [int(i) for i in line]
            data.append(new_line)
    return data



def add_weighted_average(data, weight):
    for row in data:
        total_score = row[0] * weight[0] + row[1] * weight[1]
        row.append(total_score)

def analyze_data(data):
    n = len(data)
    mean = sum(data) / n
    sum_of_squares = sum([i ** 2 for i in data])
    var = sum_of_squares / n - mean ** 2
    sorted_data = sorted(data)
    median = sorted_data[int((n - 1) / 2)] if n % 2 == 1 else (sorted_data[int(n/2 - 1)] + sorted_data[int(n/2)]) / 2
    return mean, var, median, min(data), max(data)

if __name__ == '__main__':
    data = read_data('C:/Users/박범준/GitHub/Beomjoon_Park/#3 assignment/class_score_en.csv')
    if data and len(data[0]) == 2:
        add_weighted_average(data, [40/125, 60/100])
        if len(data[0]) == 3:
            print('### Individual Score')
            print()
            print('| Midterm | Final | Total |')
            print('| ------- | ----- | ----- |')
            for row in data:
                print(f'| {row[0]} | {row[1]} | {row[2]:.3f} |')
            print()

            print('### Examination Analysis')
            col_n = len(data[0])
            col_name = ['Midterm', 'Final', 'Total']
            colwise_data = [ [row[c] for row in data] for c in range(col_n) ]
            for c, score in enumerate(colwise_data):
                mean, var, median, min_, max_ = analyze_data(score)
                print(f'* {col_name[c]}')
                print(f'  * Mean: **{mean:.3f}**')
                print(f'  * Variance: {var:.3f}')
                print(f'  * Median: **{median:.3f}**')
                print(f'  * Min/Max: ({min_:.3f}, {max_:.3f})')


