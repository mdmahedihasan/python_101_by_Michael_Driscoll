import csv


def csv_reader(file_obj):
    """
    Read a csv file
    :param file_obj: 
    :return: 
    """
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))

if __name__ == "__main__":
    csv_path = "data.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)