# 🎓 Student Management System

A web-based **Student Management System** developed using Python, FastAPI, SQLite, HTML, CSS, and Jinja2. This application helps manage student records efficiently with complete CRUD operations and attendance management.

## 🚀 Features

- **Add Students:** Register new students with their personal and academic details.
- **View Students:** Display all registered student records.
- **Student Details:** View individual student information.
- **Update Students:** Edit existing student details.
- **Delete Students:** Remove student records.
- **Attendance Management:** Track student attendance.
- **Present Students:** Display students marked present.
- **Absent Students:** Display students marked absent.
- **Database Integration:** Store and manage student information using SQLite.
- **Data Validation:** Validate student inputs using Pydantic.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | Web framework |
| SQLite | Database |
| HTML | Page structure |
| CSS | Styling |
| Jinja2 | Dynamic HTML templates |
| Pydantic | Data validation |

## 📂 Project Structure

```text
Student-Management-System/
│
├── main.py
│
├── students.db
│
├── templates/
│   ├── home.html
│   ├── add-student.html
│   ├── update-std.html
│   ├── single-std.html
│   ├── std-present.html
│   └── std-absent.html
│
├── requirements.txt
│
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/saibhushan2005/Student-Management-System.git
```

### 2. Navigate to the Project Folder

```bash
cd Student-Management-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Required Packages

```bash
pip install fastapi uvicorn jinja2 python-multipart
```

### 6. Run the Application

```bash
uvicorn main:app --reload
```

### 7. Open in Browser

```text
http://127.0.0.1:8000
```

## 🔗 Application Routes

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | View all students |
| GET | `/students/add` | Open add student form |
| POST | `/students/add` | Add a student |
| GET | `/student/{std_id}` | View student details |
| GET | `/student/edit/{std_id}` | Open edit form |
| POST | `/student/edit/{std_id}` | Update student |
| POST | `/std/delete/{std_id}` | Delete student |
| GET | `/students/present` | View present students |
| GET | `/students/absent` | View absent students |

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Developing web applications using FastAPI.
- Implementing CRUD operations.
- Connecting Python with SQLite.
- Creating dynamic web pages using Jinja2.
- Handling HTTP methods and API routes.
- Validating user input using Pydantic.
- Managing student records efficiently.

## 🎯 Project Objective

The main objective of this project is to simplify student record management by providing an easy-to-use web application for adding, viewing, updating, deleting, and tracking student information.

## 👨‍💻 Developer

**Pilla Sai Bhushan**

GitHub: [@saibhushan2005](https://github.com/saibhushan2005)

**Project Repository:**  
[Student Management System](https://github.com/saibhushan2005/Student-Management-System)

---

⭐ If you find this project useful, feel free to star the repository!

**Built with Python and a passion for learning! 🚀**
