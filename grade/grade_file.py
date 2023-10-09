my_file = open("grade of stuent.txt","w")
ns = int(input("enter a no of students :  "))
for i in range(ns):
    std_id = (input("enter id of a student :"))
    std_name = input("enter name of a student :")
    std_grade = (input("enter grade of a student :"))
    my_file.write(std_id+"\t")
    my_file.write(std_name+'\t')
    my_file.write(std_grade+'\t'+'\n')

my_file.close()