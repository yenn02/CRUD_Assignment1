# CRUD_Assignment1
A web application that allows the user( as admin) to drop/add a student from a course, CRUD to all collections in the database
# CRUD_database
A simple web application that interacts with the MongoDB database

1) **How to run the web application**
  a) run the web application in a virtual environment by **python run.py**

  b) install the following libraries if needed:
  
    i) install flask: **python -m pip install flask**
    
    ii) install pyMongo in the flask: **$ pip install Flask-PyMongo**
   
2)**Navigating through the web**
   a) **Student page**: The user/admin can check the list of students in the system, and can add, and remove students. Also, the admin can update all student's data
   
   b) **Instructor**: The user/admin can check the list of instructors in the system, and can add, or remove instructors. Also, the admin can update all Instructor's data
   
   c) **Courses**: Students can drop the courses from the enrolled list. The program deletes selected courses from the enrollment collection.
   
       i) **Course List**: display courses in the systems. the admin/user can add, remove, update more course (the program will check if a course or instructor exist)
       
       ii) **Enrollment**: display the students in the selected course, and allow admin to add or drop students from the course. Also, Admin will have to update the student's credit for the course.
