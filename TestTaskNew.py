import csv
from collections import defaultdict
from datetime import datetime, timedelta


def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    data_read = [row for row in reader]
    return data_read


if __name__ == "__main__":
    csv_path = "trades.csv"

    with open(csv_path, "r") as f_obj:
        data = csv_reader(f_obj)

    # choose needed data: ['exchange','time']
    data = [item[::-3] for item in data]
    data.sort(key=lambda i: i[0])

    # form data_dict - dictionary of our exchanges
    data_dict = defaultdict(list)
    for key, value in data:
        data_dict[key].append(value)

    # for each key of data_dict make its col_time and search one-minute window in it
    for i in range(len(data_dict)):
        number = 0
        col_time = list(data_dict.values())[i]
        times = []
        for d in col_time:
            times.append(datetime.strptime(d, "%H:%M:%S.%f"))

        qty = 0
        j = 0
        done = False
        timeMinute = timedelta(minutes=1)
        # d - each in len(times); j refers to the position, where we stopped the last time
        for d in range(len(times)):
            if done:
                break
            while times[j] - times[d] < timeMinute:
                j = j + 1
                if j == len(times) - 1:
                    if times[j] - times[d] >= timeMinute:
                        j = j - 1
                    done = True
                    break
                if times[j] - times[d] >= timeMinute:
                    j = j - 1
                    break
            qty = max(qty, j - d + 1)

        print(qty)
