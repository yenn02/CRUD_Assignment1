from application import app
from flask import render_template, request, redirect, flash, url_for, session

from bson import ObjectId

from .forms import SignIn, Credit, AddCourse, AddInstructor
from application import db
from datetime import datetime

# ----------------------------------Student add, update, delete and create -------------------
@app.route("/add_student", methods = ['POST', 'GET'])
def add_student():
    if request.method == "POST":
        form = SignIn(request.form)
        student_name = form.student_name.data
        student_id = form.student_id.data
        credit = form.credit.data
        session['student_id'] = student_id
        # check if student already existed
        if (db.students.count_documents({'student_id': student_id}, limit = 1)):
            flash("ID already exist successfully")
            return redirect("/")

        else:
            db.students.insert_one({
                "student_name": student_name,
                "student_id": student_id,
                "total_credit": credit,
            
            })

            flash("Student successfully added", "success")
            return redirect("/")
       
    else:
        form = SignIn()
    return render_template("sign_in.html", form = form)
# --------------------------update student information
@app.route("/update_profile/<id>", methods = ['POST', 'GET'])
def update_profile(id):
     if request.method == "POST":
         form = SignIn(request.form)
         student_name = form.student_name.data
         student_id = form.student_id.data
         credit = form.credit.data
       
         if (db.students.count_documents({'student_id': student_id}, limit = 1)):
            db.students.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
                "student_name": student_name,
                "student_id": student_id,
                "total_credit": credit,
            }})
            flash("Successfully updated student profile", "success")
            return redirect("/")
     else:
         form = SignIn()

       
     return render_template("sign_in.html", form = form)
# ------------display student data-------------
@app.route("/")
def get_students():
    # instructors = []
    students = []
    for student in db.students.find().sort("student_name", 1):
        student["_id"] = str(student["_id"])
        students.append(student)
 

    return render_template("view_students.html", students = students)
# -------------------delete selected student ------------------
@app.route("/delete_student/<id>")
def delete_student(id):
    db.students.find_one_and_delete({"_id": ObjectId(id)})
    flash("Student successfully deleted", "success")
    return redirect("/")

#-------------------------add course when button clicked-------------

@app.route("/add_course", methods = ['POST', 'GET'])
def add_course():
    if request.method == "POST":
        form = AddCourse(request.form)
        course_name = form.course_name.data
        course_id = form.course_id.data
        ins_id = form.ins_id.data
        # check if course already existed
        if (db.courses.count_documents({'course_id': course_id}, limit = 1)):
            flash("Course already existed")
            return redirect("/get_course")

        else:
            # check if the instructor existed, if yes, insert course; if no, redirect to instructor page
            if (db.instructor.count_documents({'ins_id': ins_id}, limit = 1)):
          
                db.courses.insert_one({
                    "course_id": course_id,
                    "course_name": course_name,
                    "ins_id": ins_id,
                })
                flash("Successfully added course", "success")
                return redirect("/get_course")
            else:
                flash("Instructor ID doesn't exist", "failed")
                return redirect("/get_instructor")
         

       
    else:
        form = AddCourse()
    return render_template("add_course.html", form = form)
# -------------update course information-------------
@app.route("/update_course/<id>", methods = ['POST', 'GET'])
def update_course(id):
     if request.method == "POST":
         form = AddCourse(request.form)
         course_name = form.course_name.data
         course_id = form.course_id.data
         ins_id = form.ins_id.data
        #  check if the updated information is valid (if instructor existed)
         if (db.instructor.count_documents({'ins_id': ins_id}, limit = 1)):
          
            db.courses.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
                "course_name": course_name,
                "course_id": course_id,
                "ins_id": ins_id,
            }})
            flash("Successfully updated student profile", "success")
            return redirect("/")
         else:
            flash("Instructor ID doesn't exist", "failed")
            return redirect("/get_instructor")
         
     else:
         form = AddCourse()

       
     return render_template("add_course.html", form = form)

# --------------dipslay course ----------
@app.route("/get_course")
def get_course():
    # instructors = []
    courses = []
    instructor = []
    for course in db.courses.find().sort("course_name", 1):
        course["_id"] = str(course["_id"])
        courses.append(course)
    for person in db.instructor.find():
        person["_id"] = str(person["_id"])
        instructor.append(person)

    return render_template("view_courses.html", courses = courses, instructor = instructor)
# ------------delete selected course-----------
@app.route("/drop_course/<id>")
def drop_course(id):
    db.courses.find_one_and_delete({"_id": ObjectId(id)})
    flash("Course successfully deleted", "success")
    return redirect("/get_course")

# -----------display instructors in the database---------
@app.route("/get_instructor")
def get_instructor():
    instructors = []
    for person in db.instructor.find().sort("ins_name", 1):
        person["_id"] = str(person["_id"])
        instructors.append(person)
 

    return render_template("view_instructor.html", instructors = instructors)

# ------------add instructor, also check if Intructor already existed---------
@app.route("/add_instructor", methods = ['POST', 'GET'])
def add_instructor():
    if request.method == "POST":
        form = AddInstructor(request.form)
        ins_name = form.ins_name.data
        ins_id = form.ins_id.data
        department = form.department.data
        if (db.instructor.count_documents({'ins_id': ins_id}, limit = 1)):
            flash("Instructor already existed")
            return redirect("/get_instructor")

        else:
            db.instructor.insert_one({
                "ins_name": ins_name,
                "ins_id": ins_id,
                "deparment": department,
            
            })

            flash("Insturctor successfully added", "success")
            return redirect("/get_instructor")
       
    else:
        form = AddInstructor()
    return render_template("add_instructor.html", form = form)
# ---------delete instructor -------------
@app.route("/delete_instructor/<id>")
def delete_instructor(id):
    db.instructor.find_one_and_delete({"_id": ObjectId(id)})
    flash("Instructor successfully deleted", "success")
    return redirect("/get_instructor")

# ----------update instructor------------
@app.route("/update_instructor/<id>", methods = ['POST', 'GET'])
def update_instructor(id):
     if request.method == "POST":
         form = AddInstructor(request.form)
         ins_name = form.ins_name.data
         ins_id = form.ins_id.data
         deparment = form.department.data

         db.instructor.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
            "ins_name": ins_name,
            "ins_id": ins_id,
            "department": deparment,
        }})
         flash("Successfully updated instructor profile", "success")
         return redirect("/get_instructor")
    
         
     else:
         form = AddInstructor()

       
     return render_template("add_instructor.html", form = form)

# --------display the enrolled students in each course-----------
@app.route("/view_enroll/<id>", methods = ['POST', 'GET'])
def view_enroll(id):
    session['course_id'] = 0
    courses = []
    for course in db.courses.find().sort("course_name", 1):
        if course["_id"] == ObjectId(id):
            session['course_id'] = course["course_id"]
        courses.append(course)
        
    return redirect("/enroll_list")
#-----display course page ------------   
@app.route("/enroll_list", methods = ['POST', 'GET'])
def enroll_list():
    course_id = session['course_id']
    courses = []
    enrollment = []
    students = []
    for course in db.courses.find().sort("course_name", 1):
        course["_id"] = str(course["_id"])
        courses.append(course)
    for enroll in db.enrollment.find():
        enroll["_id"] = str(enroll["_id"])
        enrollment.append(enroll)
    for student in db.students.find():
        student["_id"] = str(student["_id"])
        students.append(student)
    return render_template("view_profile.html", students = students, course_id = course_id, enrollment = enrollment, courses = courses)
# ----------update student's GPA------------
@app.route("/update_credit/<id>", methods = ['POST', 'GET'])
def update_credit(id):
     if request.method == "POST":
         form = Credit(request.form)
         credit = form.credit.data
       
    
         db.enrollment.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
             "credit": credit,
         }})
         flash("Successfully updated grade", "success")
         return redirect("/enroll_list")
     else:
         form = Credit()

     return render_template("update_credit.html", form = form)

# -----------remove student from the course----------
@app.route("/delete_enrolled/<id>")
def delete_enrolled(id):
    db.enrollment.find_one_and_delete({"_id": ObjectId(id)})
    flash("Student successfully removed from course", "success")
    return redirect("/enroll_list")
# --------add student to the course--------
@app.route("/add_enroll/<id>", methods = ['POST', 'GET'])
def add_enroll(id):
    if request.method == "POST":
        form = SignIn(request.form)
        student_name = form.student_name.data
        student_id = form.student_id.data
        credit = form.credit.data
    #    check if student already in class
        if (db.enrollment.count_documents({'student_id': student_id, 'course_id': id}, limit = 1)): 
            flash("Student is already in class")
            return redirect("/enroll_list")

        else:
            # if student already existed but not in class
            if (db.students.count_documents({'student_id': student_id}, limit = 1)): 
                db.enrollment.insert_one({
                "course_id": id,
                "student_id": student_id
                
            
                })
            else:
                # if student is not in the system, add student to the student collection and enrollment at the same time
                db.students.insert_one({
                    "student_name": student_name,
                    "student_id": student_id,
                    "total_credit": credit
                })
                db.enrollment.insert_one({
                "course_id": id,
                "student_id": student_id
                
            
                })
                           
        
        flash("Student successfully added to class", "success")
        return redirect("/enroll_list")
    else:
        form = SignIn()
    return render_template("sign_in.html", form = form)

