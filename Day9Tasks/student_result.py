# Student Result Generator.
# A school system calculates student results differently depending on available data.Create a Result class where a method can calculate the result using either two 
# subjects or three subjects.

class Result:
    def calculate(self, m1, m2, m3=0):
        total = m1 + m2 + m3
        print("Total Marks:", total)

r = Result()
r.calculate(80, 90)
r.calculate(80, 90, 85)
