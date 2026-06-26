from app.database import Base, engine
from app.models.student import Student

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")