import csv
def Gold():
    csv_file = csv.reader(open('user.csv'), delimiter=";")
    lines = list(csv_file)
    uname = input("masukan uname:")
    for row in lines:
        if row[3] == uname and row[5] == ' user':
            if (int(row[6]) >= 10000):
                row[5] = 'gold'
                row[6] = (int(row[6]) - 10000)

    print(lines)
Gold()
