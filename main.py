import pandas as pd

df = pd.read_excel('sinif.xlsx')
student_list = df.values.tolist()

number = 2021302129

for i in student_list:
    if i[0] == number:
        for x in range(len(i)):
            print(i[x])

#Ust basit, alt kompleks. aşağıdaki bölümü arkadaşımla yazdık.

import enum


class location(enum.Enum):
    unk = "Unknown"
    online = "Çevrimiçi"
    kilyos = "Kilyos"
    kampus = "Güney veya Kuzey"


class student:
    num : int = 0
    lev = ""
    sec : int = 0
    loc : location = location.unk

    def __init__(self, number, level, section, location):
        self.num = number
        self.lev = level
        self.sec = section
        self.loc = location

    def __repr__(self):
        return str(self.num) + "\n" + str(self.lev) + "\n" + str(self.sec) + "\n" + self.loc.value


class school:
    students : list[student] = []

    def __init__(self, student_list):
        for st in student_list:
            loc : location = location.unk

            loc_string = st[3]

            if loc_string == "GÜNEY veya KUZEY":
                loc = location.kampus
            elif loc_string == "SARITEPE":
                loc = location.kilyos
            elif loc_string == "ÇEVRİMİÇİ":
                loc = location.online

            self.students.append(student(st[0], st[1], st[2], loc))

    def find_student_by_number(self, number):
        for st in self.students:
            if st.num == number:
                return st

        return "Not Found"

    def find_students_by_level(self, lev):
        sts_lev = []

        for st in self.students:
            if st.lev == lev:
                sts_lev.append(st)

        return sts_lev


boun_prep = school(student_list)
print(boun_prep.find_student_by_number(2021302129))










