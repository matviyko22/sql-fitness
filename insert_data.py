from faker import Faker
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from create import User, Workout, WorkoutType, Nutrition, Sleep, Wellbeing, HealthMetric, Goal

# Initialize the Faker library
fake = Faker()

# Create a SQLAlchemy session
engine = create_engine('sqlite:///app.db')
session = Session(bind=engine)

# Query the users table
users = session.query(User).all()

# Define some different types of workouts
workout_types = ['Running', 'Weightlifting', 'Yoga', 'Swimming', 'Cycling']

# Define some realistic fitness goals
goals = ['Lose weight', 'Build muscle', 'Improve endurance', 'Increase flexibility']

# Add these goals to the Goal table
for goal in goals:
    goal_record = Goal(goal=goal)
    session.add(goal_record)

# Add these workout types to the WorkoutType table
for workout_type in workout_types:
    workout = WorkoutType(type=workout_type)
    session.add(workout)

# Generate mock data for 10 users
for _ in range(10):
    user = User(
        name=fake.name(),
        age=fake.random_int(min=18, max=80),
        gender=fake.random_element(elements=('Male', 'Female')),
        weight=fake.random_int(min=50, max=100),
        height=fake.random_int(min=150, max=200)
    )
    session.add(user)

# Generate mock data for 50 workouts
for _ in range(50):
    workout = Workout(
        user_id=fake.random_int(min=1, max=10),
        workout_type_id=fake.random_int(min=1, max=5),  # Reference the workout types
        duration=fake.random_int(min=10, max=120),
        intensity=fake.random_element(elements=('Low', 'Medium', 'High')),
        calories_burned=fake.random_int(min=100, max=1000)
    )
    session.add(workout)

# Generate mock data for 50 nutrition logs
for _ in range(50):
    nutrition = Nutrition(
        user_id=fake.random_int(min=1, max=10),
        calorie_intake=fake.random_int(min=500, max=3000),
        protein=fake.random_int(min=10, max=200),
        carbs=fake.random_int(min=10, max=300),
        fats=fake.random_int(min=10, max=100),
        micronutrients=fake.sentence(nb_words=5)
    )
    session.add(nutrition)

# Generate mock data for 50 sleep logs
for _ in range(50):
    sleep = Sleep(
        user_id=fake.random_int(min=1, max=10),
        total_sleep_time=fake.random_int(min=4, max=12),
        light_sleep=fake.random_int(min=1, max=6),
        deep_sleep=fake.random_int(min=1, max=6),
        REM_sleep=fake.random_int(min=1, max=6)
    )
    session.add(sleep)

# Generate mock data for 50 wellbeing logs
for _ in range(50):
    wellbeing = Wellbeing(
        user_id=fake.random_int(min=1, max=10),
        meditation_duration=fake.random_int(min=5, max=60),
        breathing_practice_frequency=fake.random_int(min=1, max=7)
    )
    session.add(wellbeing)

# Generate mock data for 50 health metrics logs
for _ in range(50):
    health_metric = HealthMetric(
        user_id=fake.random_int(min=1, max=10),
        body_fat_percentage=fake.random_int(min=10, max=30),
        heart_rate=fake.random_int(min=60, max=100),
        blood_pressure=fake.random_int(min=80, max=120)
    )
    session.add(health_metric)

# Commit the session to insert the mock data
session.commit()