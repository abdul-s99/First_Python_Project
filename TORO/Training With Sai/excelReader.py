import ExcelLoader as EL


class RdMember(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    a = 10
    b = "abdul"
    c = "sai"
    d = 15
    path = r"C:\Users\Abdul.Sharif\PycharmProjects\First_Python_Project\TORO\Training With Sai\STRUCTURAL REPORTS.csv"
    Abdul = RdMember(b, a)

    excel = EL.CSVtoARRAY(path)

    arrayImWorkingWith = excel.array

    counter = 0
    for row in arrayImWorkingWith:
        counter += 1
        test = row[-1]  # Get the last element of the row
        if test != "TRUE":
            print(f"Row {counter} is false.")

        # print(f"now working with row:{counter}")

    print("Your code worked")
