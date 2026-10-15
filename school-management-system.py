class Course:
    id:int=0
    name:str=""
    units:int=0
    score:float=0.0
    def __init__(self,id:int,name:str,units:int,score:float):
        self.id=id
        self.name=name
        self.units=units
        self.score=score
    def __eq__(self,other):
        return self.id==other
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.units}"
class Student:
    id:int=0
    name:str=""
    family:str=""
    courses:list=[]
    def __init__(self,id:int,name:str,family:str):
        self.name=name
        self.id=id
        self.family=family
        self.courses=[]
    def __eq__(self,other):
        return self.id==other
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.family}"
    def print_info_selected_student(self):
        print(f"id:{self.id}\nname:{self.name}\nfamily:{self.family}\ncourses:")
        print("id\tname\tunits\tscore")
        for detail in self.courses:
            print(f"{detail.id}\t{detail.name}\t{detail.units}\t{detail.score}")
    def add_course(self,selected_course):
        if selected_course in self.courses:
            print("this course already exist")
        else:
             self.courses.append(selected_course)
    def delete_course(self, course_id):
        if course_id not in self.courses:
            print("course doesnt exis")
        else:
            selected_course=self.courses[self.courses.index(course_id)]
            self.courses.remove(selected_course)
    def add_course_to_select(self,all_course):
        print(f"id\tname\tunits")
        for course in all_course:
            print(course)
        course_id=int(input("enter course id:"))
        if course_id not in all_course:
            print("course doesnt exis")
            print(f"id\tname\tunits\tscore")
            for already in all_course:
                if already not in self.courses:
                    print(f"{already.id}\t{already.name}\t{already.units}\t{already.score}")
        else:
            selected_course= all_course[all_course.index(course_id)]
            self.add_course(selected_course)
    def delete_course_to_select(self):
        print(f"id\tname\tunits\tscore")
        for detail in self.courses:
            print(f"{detail.id}\t{detail.name}\t{detail.units}\t{detail.score}")
        course_id=int(input("enter course id:"))
        self.delete_course(course_id)
    def set_score(self):
        print(f"id\tname\tunits\tscore")
        for detail in self.courses:
            print(f"{detail.id}\t{detail.name}\t{detail.units}\t{detail.score}")
        for name_course in self.courses:
            print(f"{name_course.name}:",end="")
            new_score=float(input())
            name_course.score=new_score
class Teacher:
    id:int=0
    name:str=""
    family:str=""
    courses:list=[]
    grade:str=""
    def __init__(self,id:int,name:str,family:str,grade:str):
        self.id=id
        self.name=name
        self.family=family
        self.grade=grade
        self.courses=[]
    def __eq__(self,other):
        return self.id==other
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.family}\t{self.grade}"
    def print_info_selected_teacher(self):
        print(f"id:{self.id}\nname:{self.name} \nfamily:{self.family}\ngrade:{self.grade}\ncourses:")
        print(f"id\tname\tunits\tscore")
        for detail in self.courses:
            print(f"{detail.id}\t{detail.name}\t{detail.units}\t{detail.score}")
    def add_course_to_select(self,all_course):
        print(f"id\tname\tunits")
        for course in all_course:
            print(course)
        course_id=int(input("enter course id:"))
        if course_id not in all_course:
            print("course doesnt exis")
        else:
            selected_course= all_course[all_course.index(course_id)]
            if selected_course in self.courses:
                print("this course already exist")
                print(f"id\tname\tunits\tscore")
                for already in all_course:
                    if already not in self.courses:
                        print(f"{already.id}\t{already.name}\t{already.units}\t{already.score}")
            else:
                self.courses.append(selected_course)
    def delete_course_to_select(self):
            print(f"id\tname\tunits\tscore")
            for detail in self.courses:
                print(f"{detail.id}\t{detail.name}\t{detail.units}\t{detail.score}")
            course_id=int(input("enter course id:"))
            if course_id not in self.courses:
                print("course doesnt exis")
            else:
                selected_course=self.courses[self.courses.index(course_id)]
                self.courses.remove(selected_course)
class Classroom:
    id:int=0
    name:str=""
    course:Course=None
    teacher:Teacher=None
    students:Student=[]
    def __init__(self,id:int,name:str):
        self.id=id
        self.name=name
        self.course = None
        self.teacher = None
        self.students = []
    def __eq__(self,other):
        return self.id==other
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.course.name}\t{self.teacher.name} {self.teacher.family}\t{len(self.students)}"
    def print_info_selected_classroom(self):
        if self.teacher is not None:
            teacher_info=f"{self.teacher.name}{self.teacher.family}"
        else:
            teacher_info ="None"
        print(f"id:{self.id}\nname:{self.name} \ncourses:{self.course.name} \nteachers:{teacher_info}\nstudents:")  
        print(f"id\tname\tfamily")
        for detail in self.students:
            print(f"{detail.id}\t{detail.name}\t{detail.family}")
    def change_course(self,all_course):
        print("id\tname\tunits")
        for course in all_course:
            print(f"{course.id}\t{course.name}\t{course.units}")
        id_cuorse=int(input("enter course id: "))
        selected_course = all_course[all_course.index(id_cuorse)]
        self.course = selected_course
        if selected_course not in self.teacher.courses:
            self.teacher = None
        valid_students=[]
        for student in self.students:
            if selected_course in student.courses:
                valid_students.append(student)
        self.students = valid_students
    def change_teacher(self,all_teacher):
        print("id\tname\tfamily\tgrade")
        for teacher in all_teacher:
            if self.course in teacher.courses:
                print(f"{teacher.id}\t{teacher.name}\t{teacher.family}\t{teacher.grade}")
        id_teacher=int(input("enter teacher id: "))
        selected_teacher = all_teacher[all_teacher.index(id_teacher)]
        self.teacher = selected_teacher
    def add_student(self,all_student):
        student_under_ten=[]
        selected_course = self.course
        for student in all_student:
            if selected_course in student.courses:
                student_course =student.courses[student.courses.index(selected_course)]
                if student_course.score < 10 and student not in self.students :
                    student_under_ten.append(student)
        print("id\tname\tfamily")
        for student in student_under_ten:
            print(f"{student.id}\t{student.name}\t{student.family}")
        student_id=int(input("enter student id: "))
        selected_student= student_under_ten[student_under_ten.index(student_id)]
        self.students.append(selected_student)
    def remove_student(self):
        print("id\tname\tfamily")
        for student in self.students:
            print(f"{student.id}\t{student.name}\t{student.family}")
        student_id=int(input("enter student id: "))
        selected_student= self.students[self.students.index(student_id)]
        self.students.remove(selected_student)

class School:
    name:str=""
    courses:list=[]
    teachers:list=[]
    students:list=[]
    classrooms:list=[]
    selected_student:Student=None
    selected_teacher:Teacher=None
    selected_classroom:Classroom=None
    def __init__(self,name:str):
        self.name=name
    def add_student(self,student):
        if student in self.students:
            print("student already exits")
        else:
            self.students.append(student)
    def add_teacher(self,teacher):
        if teacher in self.teachers:
            print("teacher already exits")
        else:
            self.teachers.append(teacher)
    def add_course(self,course):
        if course in self.courses:
            print("course already exits")
        else:
            self.courses.append(course)
    def add_classroom(self,classroom):
        if classroom in self.classrooms:
            print("classroom already exits")
        else:
            self.classrooms.append(classroom)
    def print_student(self):
        print("id\tname\tfamily")
        for student in self.students:
            print(student)
    def print_teacher(self):
        print("id\tname\tfamily\tgrade")
        for teacher in self.teachers:
            print(teacher)
    def print_course(self):
        print("id\tname\tunits")
        for course in self.courses:
            print(course)
    def print_classroom(self):
        print("id\tname\tcourse\tteacher\tstudents")
        for classroom in self.classrooms:
            print(classroom)
    def remove_student(self,id):
        if id not in self.students:
            print("student doesnt exits")
        use_student_id=[]
        for find_student in self.classrooms:
            use_student_id=[student.id for student in find_student.students]
        if id in use_student_id:
            print("this student already use in classroom")
        else:
            self.students.remove(id)
    def remove_teacher(self,id):
        if id not in self.teachers:
            print("teacher doesnt exits")
        use_teacher_id=[find_teacher.teacher.id for find_teacher in self.classrooms]
        if id in use_teacher_id:
            print("this teacher already use in classroom")
        else:
            self.teachers.remove(id)
    def remove_course(self,id):
        if id not in self.courses:
            print("course doesnt exits")
        use_in_teacher = [find_course.id for find_teacher in self.teachers for find_course in find_teacher.courses ]
        use_in_student = [find_course.id for find_student in self.students for find_course in find_student.courses ]
        use_in_classroom = [find_classroom.course for find_classroom in self.classrooms]
        if id in use_in_student or id in use_in_teacher or id in use_in_classroom:
            print("this course already use")
        else:
            self.courses.remove(id)
    def remove_classroom(self,id):
        if id not in self.classrooms:
            print("classroom doesnt exits")
        else:
            self.classrooms.remove(id)
    def edit_student(self,student):
        if student not in self.students:
            print("student doesnt exits")
        else:
            self.students[self.students.index(student)]=student
    def edit_teacher(self,teacher):
        if teacher not in self.teachers:
            print("teacher doesnt exits")
        else:
            self.teachers[self.teachers.index(teacher)]=teacher
    def edit_course(self,course):
        if course not in self.courses:
            print("course doesnt exits")
        else:
            self.courses[self.courses.index(course)]=course
    def edit_classroom(self,classroom):
        if classroom not in self.classrooms:
            print("classroom doesnt exits")
        else:
            self.classrooms[self.classrooms.index(classroom)]=classroom
    def load_data(self):
        import json
        with open ("d3.json","rt") as f1:
            s=f1.read()
        data_jsons=json.loads(s)
        for data_json in data_jsons["courses"]:
            self.courses.append(Course(data_json["id"],data_json["name"],data_json["units"],data_json["score"]))
        for data_json in data_jsons["students"]:
            st1=Student(data_json["id"],data_json["name"],data_json["family"])
            for raw_course in data_json["courses"]:
                course_id=raw_course[0]
                course_score=raw_course[1]
                if course_id in self.courses:
                    load_course=self.courses[self.courses.index(course_id)]
                    main_load_course=Course(load_course.id,load_course.name,load_course.units,course_score)
                    st1.courses.append(main_load_course)
            self.students.append(st1)
        for data_json in data_jsons["teachers"]:
            t1=Teacher(data_json["id"],data_json["name"],data_json["family"],data_json["grade"])
            for course_id in data_json["courses"]:
                if course_id in self.courses:
                    load_course=self.courses[self.courses.index(course_id)]
                    t1.courses.append(load_course)
            self.teachers.append(t1)
        for data_json in data_jsons["classrooms"]:
            cl1=Classroom(data_json["id"],data_json["name"])
            if data_json["course"] in self.courses:
                cl1.course =self.courses[self.courses.index(data_json["course"])]
            if data_json["teacher"] in self.teachers:
                cl1.teacher =self.teachers[self.teachers.index(data_json["teacher"])]
            for classroom_student_id in data_json["students"]:
                if classroom_student_id in self.students:
                    load_classrooms=self.students[self.students.index(classroom_student_id)]
                    cl1.students.append(load_classrooms)
            self.classrooms.append(cl1)
    def save_data(self):
        import json
        result={"students":[],"teachers":[],"courses":[],"classrooms":[]}
        with open ("d3.json","wt") as f2:
            for student in self.students:
                json_student={"id":student.id,"name":student.name,"family":student.family,"courses":[[s.id,s.score] for s in student.courses]}
                result["students"].append(json_student)
            for teacher in self.teachers:
                json_teacher={"id":teacher.id,"name":teacher.name,"family":teacher.family,"grade":teacher.grade,"courses":[t.id for t in teacher.courses]}
                result["teachers"].append(json_teacher)
            for course in self.courses:
                json_course={"id":course.id,"name":course.name,"units":course.units,"score":course.score}
                result["courses"].append(json_course)
            for classroom in self.classrooms:
                json_classroom={"id":classroom.id,"name":classroom.name,"course":classroom.course.id,"teacher":classroom.teacher.id,"students":[s.id for s in classroom.students]}
                result["classrooms"].append(json_classroom)
            s=json.dumps(result)
            f2.write(s)


level="root"
sc1 = School("sama")
sc1.load_data()
while True:
    if level=="root":
        print("1.students")
        print("2.teachers")
        print("3.courses")
        print("4.classrooms")
        print("5.save")
        print("0.exit")
        cmd=int(input("choose your option:"))
        if cmd==1:
            level="students"
        elif cmd==2:
            level="teachers"
        elif cmd==3:
            level="courses"
        elif cmd==4:
            level="classrooms"
        elif cmd==5:
            sc1.save_data()
        elif cmd==0:
            break
    elif level=="students":
        print("1.show student")
        print("2.add student")
        print("3.edit student")
        print("4.delete student")
        print("5.select student")
        print("0.back")
        cmd=int(input("choose your option:"))
        if cmd == 1:
            sc1.print_student()
        elif cmd ==2:
            id = int(input("id:"))
            name = input("name:")
            family = input("family:")
            sc1.add_student(Student(id,name,family))
        elif cmd ==3:
            id = int(input("id:"))
            name = input("name:")
            family = input("family:")
            sc1.edit_student(Student(id,name,family))
        elif cmd ==4:
            id = int(input("id:"))
            sc1.remove_student(id)
        elif cmd ==5:
            sc1.print_student()
            student_id=int(input("enter student id:"))
            if student_id not in sc1.students:
                print("student doesnt exis")
            else:
                sc1.selected_student=sc1.students[sc1.students.index(student_id)]
                level="student_select"
        elif cmd ==0:
            level="root"
    elif level=="student_select":
        print("1.info")
        print("2.add course")
        print("3.delete course")
        print("4.set scores")
        print("0.back")
        cmd=int(input("choose your option:"))
        if cmd ==1:
            sc1.selected_student.print_info_selected_student()
        elif cmd ==2:
            sc1.selected_student.add_course_to_select(sc1.courses)
        elif cmd ==3:
            sc1.selected_student.delete_course_to_select()
        elif cmd ==4:
            sc1.selected_student.set_score()
        elif cmd ==0:
            level="students"
    elif level=="teachers":
        print("1.show teacher")
        print("2.add teacher")
        print("3.edit teacher")
        print("4.delete teacher")
        print("5.select teacher")
        print("0.back")
        cmd=int(input("choose your option:"))
        if cmd ==1:
            sc1.print_teacher()
        elif cmd==2:
            id = int(input("id:"))
            name = input("name:")
            family = input("family:")
            grade= input ("grade:")
            sc1.add_teacher(Teacher(id,name,family,grade))
        elif cmd==3:
            id = int(input("id:"))
            name = input("name:")
            family = input("family:")
            grade= input ("grade:")
            sc1.edit_teacher(Teacher(id,name,family,grade))
        elif cmd==4:
            id = int(input("id:"))
            sc1.remove_teacher(id)
        elif cmd==5:
            sc1.print_teacher()
            teacher_id=int(input("enter teacher id:"))
            if teacher_id not in sc1.teachers:
                print("teacher doesnt exis")
            else:
                sc1.selected_teacher=sc1.teachers[sc1.teachers.index(teacher_id)]
                level="teacher_select"
        elif cmd==0:
            level="root"
    elif level=="teacher_select":
        print("1.info")
        print("2.add course")
        print("3.delete course")
        print("0.back")
        cmd=int(input("choose your option:"))
        if cmd ==1:
            sc1.selected_teacher.print_info_selected_teacher()
        elif cmd ==2:
            sc1.selected_teacher.add_course_to_select(sc1.courses)
        elif cmd ==3:
            sc1.selected_teacher.delete_course_to_select()
        elif cmd ==0:
            level="teachers"
    elif level=="courses":
        print("1.show courses")
        print("2.add courses")
        print("3.edit courses")
        print("4.delete courses")
        print("0.back")
        cmd=int(input("choose your option:"))
        if cmd ==1:
            sc1.print_course()
        elif cmd==2:
            id = int(input("id:"))
            name = input("name:")
            units = input("units:")
            score= input ("score:")
            sc1.add_course(Course(id,name,units,score))
        elif cmd==3:
            id = int(input("id:"))
            name = input("name:")
            units = input("units:")
            score= input ("score:")
            sc1.edit_course(Course(id,name,units,score))
        elif cmd==4:
            id = int(input("id:"))
            sc1.remove_course(id)
        elif cmd==0:
            level="root"
    elif level=="classrooms":
        print("1.show classrooms")
        print("2.add classrooms")
        print("3.edit classrooms")
        print("4.delete classrooms")
        print("5.select classrooms")
        print("0.back")
        cmd=int(input("choose your option:"))
        if cmd ==1:
            sc1.print_classroom()
        elif cmd==2:
            id=int(input("id:"))
            name=input("name:")
            c1=Classroom(id,name)
            print(f"id\tname\tunits\tscore")
            for detail in sc1.courses:
                print(f"{detail.id}\t{detail.name}\t{detail.units}\t{detail.score}")
            id_course=int(input("course:"))
            selected_course=sc1.courses[sc1.courses.index(id_course)]
            c1.course=selected_course
            print(f"id\tname\tfamily\tgrade")
            for teacher in sc1.teachers:
                if selected_course in teacher.courses:
                    print(f"{teacher.id}\t{teacher.name}\t{teacher.family}\t{teacher.grade}")
            teacher_id=int(input("teacher:"))
            selected_teacher=sc1.teachers[sc1.teachers.index(teacher_id)]
            c1.teacher=selected_teacher
            student_under_ten=[]
            for student in sc1.students:
                if selected_course in student.courses:
                    student_course=student.courses[student.courses.index(selected_course)]
                    if student_course.score < 10 :
                        student_under_ten.append(student)
            while True:
                print(f"id\tname\tfamily")
                for student in student_under_ten:
                    print(f"{student.id}\t{student.name}\t{student.family}")
                student_id= int (input("enter student id:"))
                if student_id==0:
                    break
                student_select_under_ten=student_under_ten[student_under_ten.index(student_id)]
                c1.students.append(student_select_under_ten)
                student_under_ten.remove(student_id)
            sc1.add_classroom(c1)
        elif cmd==3:
            print(f"id\tname\tcourse\tteacher\tstudent")
            for detail in sc1.classrooms:
                print(f"{detail.id}\t{detail.name}\t{detail.course.name}\t{detail.teacher.name} {detail.teacher.family}\t{len(detail.students)}")
            classroom_id=int(input("enter classroom id:"))
            if classroom_id not in sc1.classrooms:
                print("classroom doesnt exis")
            else:
                classroom_name = input("enter classroom name:")
                current_classroom=sc1.classrooms[sc1.classrooms.index(classroom_id)]
                current_classroom.name=classroom_name
                sc1.edit_classroom(current_classroom)
        elif cmd==4:
            print(f"id\tname\tcourse\tteacher\tstudent")
            for detail in sc1.classrooms:
                print(f"{detail.id}\t{detail.name}\t{detail.course.name}\t{detail.teacher.name} {detail.teacher.family}\t{len(detail.students)}")
            classroom_id=int(input("enter classroom id:"))
            if classroom_id not in sc1.classrooms:
                print("classroom doesnt exis")
            else:
                sc1.remove_classroom(classroom_id)
        elif cmd==5:
            sc1.print_classroom()
            classroom_id=int(input("enter classroom id:"))
            if classroom_id not in sc1.classrooms:
                print("classroom doesnt exis")
            else:
                sc1.selected_classroom=sc1.classrooms[sc1.classrooms.index(classroom_id)]
                level="classroom_select"
        elif cmd==0:
            level="root"
    elif level=="classroom_select":
        print("1.show info")
        print("2.change course")
        print("3.change teacher")
        print("4.add student")
        print("5.remove student")
        print("0.back")
        cmd=int(input("choose your option:"))
        if cmd ==1:
            sc1.selected_classroom.print_info_selected_classroom()
        elif cmd ==2:
            sc1.selected_classroom.change_course(sc1.courses)
        elif cmd ==3:
            sc1.selected_classroom.change_teacher(sc1.teachers)
        elif cmd ==4:
            sc1.selected_classroom.add_student(sc1.students)
        elif cmd ==5:
           sc1.selected_classroom.remove_student()
        elif cmd ==0:
            level="classrooms"