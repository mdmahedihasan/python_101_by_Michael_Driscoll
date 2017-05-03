import csv


def csv_writer(data, path):
    """
    Write data to a csv file path
    :param data: 
    :param path: 
    :return: 
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

if __name__ == "__main__":
    data = ["first_name, last_name, city".split(', '),
            "mahedi, hasan, dhaka".split(', ')]
    path = "test3.csv"
    csv_writer(data, path)