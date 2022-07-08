def Menu1(name, mid_score, final_score):
    student = dict()
    student['name'] = name
    student['mid_score'] = mid_score
    student['final_score'] = final_score
    students.append(student)


def Menu2():
    for i in students:
        if 'grade' not in i.keys():
            average = i['mid_score']+i['final_score']
            if average >= 90:
                i['grade'] = 'A'
            elif average >= 80:
                i['grade'] = 'B'
            elif average >= 70:
                i['grade'] = 'C'
            else:
                i['grade'] = 'D'

def Menu3():
    print("--------------------------------")
    print("name    mid    final    grade")
    print("-------------------------------")
    for i in students:
        print(str(i['name']+'\t'+str(i['mid_score'])+'\t'+str(i['final_score'])+'\t'+i['grade']))
                
def Menu4(name):
    for i in students:
        if i['name'] == name:
            a = i
    for j in range(len(students)):
        if students[j] == a:
            index = j
    del students[index]
            
            
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")

names= []
students = []

while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
            name, mid_score, final_score = input("Enter name mid-score final-score : ").split()
        except ValueError:
            print("Num of data is not 3!")
        else:
            try:
                mid_score = int(mid_score)
                final_score = int(final_score)
                if name in names:
                    raise Exception("Already exist name")
                if mid_score < 0 or final_score < 0:
                    raise Exception("Score is not positive integer!")
            except ValueError:
                print("Score is not positive integer!")
            except Exception as e:
                print(e)
            else:
                names.append(name)
                Menu1(name, mid_score, final_score)
                
    elif choice == "2" :
        if len(students) == 0:
            print("No student data!")
            continue
        else:
            print("Grading to all students")
            Menu2()
            
    elif choice == "3" : 
        if len(students) == 0:
            print("No student data!")
            continue
        try: 
            for i in students:
                if 'grade' not in i.keys():
                    raise Exception("There is a student who didn't get grade")
        except Exception as e:
            print(e)
        else:
            Menu3()
        
    elif choice == "4":
        if len(students) == 0:
            print("No student data!")
            continue
        else:
            name = input("Enter the name to delete : ")
        if name not in names:
            print("Not exist name!")
            continue
        else:
            Menu4(name)
            print(f"{name} student information is deleted")
            
    elif choice == "5" :
        print("Exit Program!")
        break
    
    else :
        print("Wrong number. Choose again.")
