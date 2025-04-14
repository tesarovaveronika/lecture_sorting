import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        slovnik = {}
        n=0
        for row in reader:
            if n == 0:
                parts = row.split(",")
                slovnik[parts[0]] = []
                slovnik[parts[1]] = []
                slovnik[parts[2]] = []
            else:
                casti = row.split(",")
                slovnik[parts[0]].append(int(casti[0]))
                slovnik[parts[1]].append(int(casti[1]))
                slovnik[parts[2]].append(int(casti[2]))
            n += 1
    return slovnik





def main():
    slovnik = read_data(numbers.csv)
    pass


if __name__ == '__main__':
    main()
