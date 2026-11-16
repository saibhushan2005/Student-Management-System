from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
import sqlite3
from fastapi.responses import RedirectResponse
from pydantic import BaseModel,Field

def get_connection():
    connection=sqlite3.connect(
        "students.db"
    )
    return connection
get_connection()

def create_table():
    connection=get_connection()
    cursor=connection.cursor()

    q="""
    CREATE TABLE  IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    marks INTEGER,
    course TEXT,
    image TEXT,
    status INTEGER
    )
    """

    cursor.execute(q)
    connection.commit()
    connection.close()

create_table()


templates=Jinja2Templates(
    directory="templates"
)

class student(BaseModel):
    name:str=Field(min_length=3,max_length=25)
    age:int=Field(le=60,ge=18)
    gender:str
    marks:int=Field(le=100,ge=1)
    course:str
    image:str
    status:int


app=FastAPI()

@app.get("/")
def home(req: Request):

    connection = get_connection()
    cursor = connection.cursor()

    # Get all students
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    # Get total students count
    cursor.execute("SELECT COUNT(*) FROM students")
    total = cursor.fetchone()[0]

    # cursor.execute("SELECT COUNT(*) FROM students WHERE status = 1")
    # present = cursor.fetchone()[0]

    # cursor.execute("SELECT COUNT(*) FROM students WHERE status = 0")
    # absent = cursor.fetchone()[0]

    connection.close()

    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={
            "stds": students,
            "total": total
        }
    )

@app.get("/student/{std_id}")
def singe_std(req:Request,std_id:int):

    connection=get_connection()
    cursor=connection.cursor()
    q="""
    select * from students where id=?
    """
    cursor.execute(q,(std_id,))
    student=cursor.fetchone()
    connection.close()
    return templates.TemplateResponse(
        request=req,
        name="single-std.html",
        context={
            "std":student
        }
    )

@app.post("/std/delete/{std_id}")
def std_delete(std_id:int):
    connection=get_connection()
    cursor=connection.cursor()
    q="""
    delete from students where id=?
    """
    cursor.execute(q,(std_id,))
    connection.commit()
    connection.close()
    return RedirectResponse(url="/",status_code=303)




@app.get("/students/add")
def create_student(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="add-student.html",
        context={}
    )

@app.post("/students/add")
def create_std(name=Form(),age=Form(),gender=Form(),marks=Form(),course=Form(),image=Form(),status=Form()):
    std_obj=student(
        name=name,
        age=age,
        gender=gender,
        marks=marks,
        course=course,
        image=image,
        status=status
    )

    values=(std_obj.name,std_obj.age,std_obj.gender,std_obj.marks,std_obj.course,std_obj.image,bool(std_obj.status))

    connection=get_connection()
    cursor=connection.cursor()
    q="""
    INSERT INTO students(name,age,gender,marks,course,image,status)
    values(?,?,?,?,?,?,?);
    """

    cursor.execute(q ,values)
    connection.commit()
    connection.close()
    return RedirectResponse(url="/",status_code=303)

@app.get("/student/edit/{std_id}")
def edit_std(req:Request,std_id):

    connection=get_connection()
    cursor=connection.cursor()
    q="""
    select * from students where id=?
    """
    cursor.execute(q,(std_id,))
    student=cursor.fetchone()

    return templates.TemplateResponse(
        request=req,
        name="update-std.html",
        context={
            "std":student
        }
    )

@app.post("/student/edit/{std_id}")
def update_std(
    std_id:int,
    name=Form(),
    age=Form(),
    marks=Form(),
    gender=Form(),
    course=Form(),
    image=Form(),
    status=Form(),
    ):

    std_obj=student(
        name=name,
        age=age,
        marks=marks,
        gender=gender,
        course=course,
        image=image,
        status=status
        )

    connection=get_connection()
    cursor=connection.cursor()

    q="""    
    UPDATE students 
    SET name=?,
    age=?,
    marks=?,
    gender=?,
    course=?,
    image=?,
    status=? where id=?
    """

    cursor.execute(q,(std_obj.name,std_obj.age,std_obj.marks,std_obj.gender,std_obj.course,std_obj.image,std_obj.status,std_id))
    connection.commit()
    connection.close()
    return RedirectResponse(url="/",status_code=303)


@app.get("/students/present")
def present_students(req: Request):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students WHERE status = 1")
    students = cursor.fetchall()

    connection.close()

    return templates.TemplateResponse(
        request=req,
        name="std-present.html",
        context={
            "stds": students
        }
    )


@app.get("/students/absent")
def absent_students(req: Request):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students WHERE status = 0")
    students = cursor.fetchall()

    connection.close()

    return templates.TemplateResponse(
        request=req,
        name="std-absent.html",
        context={
            "stds": students
        }
    )
