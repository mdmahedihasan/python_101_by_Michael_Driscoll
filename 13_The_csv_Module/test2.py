import csv


def csv_dict_reader(file_obj):
    """
    Read a csv file using csv.DictReader
    :param file_obj: 
    :return: 
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["first_name"])
        print(line["last_name"])

if __name__ == "__main__":
    with open("new.csv") as f_obj:
        csv_dict_reader(f_obj)