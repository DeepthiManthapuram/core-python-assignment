class student: #defining class
    def __init__(self,name):
        self.name = name

    #calculating average score of each student
    def avgCalculator(self,values):
        sum = 0
        l = len(values)
        for i in values:
            sum = sum + int(i)
        avg = sum/l
        if(avg.is_integer()):
            return int(avg)
        else:
            return round(avg,2)

dict = eval(input("students:")) #converting an input into dictionary
avg_list = {}

for name in dict.keys(): #accessing keys of dictionary
    s = student(name)
    s_avg = s.avgCalculator(dict[name])
    avg_list[name] = s_avg
print(avg_list) #printing average score of all students

max_name = max(avg_list,key = lambda k: float(avg_list[k])) #finding maximum of the averages
print("Top Performer:",max_name)


