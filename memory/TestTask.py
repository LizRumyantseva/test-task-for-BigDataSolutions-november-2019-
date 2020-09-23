import csv
from collections import defaultdict
from datetime import datetime, timedelta


def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    data_read = [row for row in reader]
    return data_read

def

if __name__ == "__main__":
    csv_path = "Trades.csv"

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

        # for d in range(len(times)):
        #     time_end = (times[d] + timedelta(minutes=1))
        #     qty = 0
        #     # find numbers of trades in each one-min window
        #     for k in range(len(times)):
        #        if times[d] <= times[k]< time_end:
        #             qty += 1
        #     # find maximum number for the key
        #     number = max(number, qty)
        print(number)
