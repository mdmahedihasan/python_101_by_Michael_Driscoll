import csv


def csv_dict_writer(path, fieldnames, data):
    """
    Writes a csv file using DictWriter
    :param path: 
    :param fieldnames: 
    :param data: 
    :return: 
    """
    with open(path, "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    data = ["first_name, last_name, city".split(','),
            "mahedi,hasan,dhaka".split(','),
            "Jules,Dicki,Lake Nickolasville".split(",")]
    my_list = []
    fieldnames = data[0]
    for values in data[1:]:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)

    path = "test4.csv"
    csv_dict_writer(path, fieldnames, my_list)