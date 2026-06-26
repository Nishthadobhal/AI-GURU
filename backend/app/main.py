from fastapi import FastAPI
from app.schemas.student import StudentCreate

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Guru Backend Running"
    }


@app.post("/students")
def create_student(student: StudentCreate):
    return {
        "message": "Student profile created",
        "student": student
    }