from app.database import Base, engine
from app.models.student import Student
from app.models.learning_event import LearningEvent
from app.models.student_profile import StudentProfile
from app.models.learning_goal import LearningGoal
from app.models.roadmap import Roadmap
from app.models.roadmap_topic import RoadmapTopic
from app.models.learning_session import LearningSession
from app.models.quiz import Quiz
from app.models.learner_state import LearnerState

from app.models.question import Question

from app.models.quiz_attempt import QuizAttempt
from app.models.conversation import Conversation

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")