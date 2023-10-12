from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, InputRequired, NumberRange
# create the filling form for add student, class, instructor 
class SignIn(FlaskForm):
    student_name = StringField('Student Name:', validators=[DataRequired()])
    student_id =   StringField('Student ID',validators=[DataRequired(), Length(min=3, max=3, message='Student ID must be 3 characters')])
    credit =    IntegerField('Total Credit:', validators=[InputRequired(), NumberRange(0,200, message="Credit must be in range of 0 - 200") ])
    submit_sign = SubmitField("Add Student")

class AddCourse(FlaskForm):
    course_name = StringField('Course Name:', validators=[DataRequired()])
    course_id =   StringField('Course ID',validators=[DataRequired(), Length(min=4, max=4, message='Course ID must be 4 characters')])
    ins_id =      StringField('Instructor ID:', validators=[DataRequired(), Length(min=3, max=3, message='Instructor ID must be 3 characters')])
    submit = SubmitField("Add Course")

class AddInstructor(FlaskForm):
    ins_name = StringField('Instructor Name:', validators=[DataRequired()])
    ins_id =      StringField('Instructor ID:', validators=[DataRequired(), Length(min=3, max=3, message='Instructor ID must be 3 characters')])
    department = StringField('Department: ', validators=[DataRequired()])
    submit= SubmitField("Add Instructor")


class Credit(FlaskForm):
    
    credit = IntegerField('GPA:', validators=[InputRequired(), NumberRange(0,4, message="Credit must be in range of 0 - 4")])
    submit = SubmitField("Update")