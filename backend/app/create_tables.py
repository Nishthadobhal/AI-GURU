from app.database import Base, engine
from app.models.student import Student
from app.models.learning_event import LearningEvent
from app.models.student_profile import StudentProfile
from app.models.learning_goal import LearningGoal

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")