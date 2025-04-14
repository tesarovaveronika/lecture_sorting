import os
import csv


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
                parts = row
                slovnik[parts[0]] = []
                slovnik[parts[1]] = []
                slovnik[parts[2]] = []
            else:
                casti = row
                slovnik[parts[0]].append(int(casti[0]))
                slovnik[parts[1]].append(int(casti[1]))
                slovnik[parts[2]].append(int(casti[2]))
            n += 1
    return slovnik

def selection_sort(seznam, directions = "ascending"):
    """

    :param seznam: seznam s numeric array
    :param str directions: string indicating sorting direction: ascending, descending
    :return: sorted seznam
    """
    for n in range(len(seznam)):
        idx = n
        for i in range(n+1,len(seznam)):
            if (directions == "ascending" and seznam[i] < seznam[idx]) or (directions == "descending" and seznam[i] > seznam[idx]):
                idx = i
        seznam[n], seznam[idx] = seznam[idx], seznam[n]
    return seznam




def main():
    slovnik = read_data("numbers.csv")
    seznam = selection_sort(slovnik["series_1"])
    print(seznam)
    print(slovnik)
    pass


if __name__ == '__main__':
    main()
