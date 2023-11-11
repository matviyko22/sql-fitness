from faker import Faker
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from create import User, Workout, WorkoutType, Nutrition, Sleep, Wellbeing, HealthMetric, Goal, user_goals
from random import choice, randint

# Initialize the Faker library
fake = Faker()

# Create a SQLAlchemy session
engine = create_engine('sqlite:///app.db')
session = Session(bind=engine)

# Define some different types of workouts
workout_types = ['Running', 'Weightlifting', 'Yoga', 'Swimming', 'Cycling']

# Define some realistic fitness goals
goals = ['Lose weight', 'Build muscle', 'Improve endurance', 'Increase flexibility']

# Add these goals to the Goal table and store them in a list for later use
goal_records = []
for goal in goals:
    goal_record = Goal(goal=goal)
    goal_records.append(goal_record)
    session.add(goal_record)

# Add these workout types to the WorkoutType table
for workout_type in workout_types:
    workout = WorkoutType(type=workout_type)
    session.add(workout)

# Hardcoding the names of 30 users for testing purposes
names = ['John', 'Jane', 'Bob', 'Alice', 'Charlie', 'Sophie', 'Max', 'Olivia', 'James', 'Emily', 'Michael', 'Sarah', 'Jacob', 'Emma', 'Noah', 'Ava', 'William', 'Isabella', 'Ethan', 'Sophia', 'James', 'Mia', 'Alexander', 'Charlotte', 'Mason', 'Amelia', 'Henry', 'Harper', 'Benjamin', 'Evelyn']

# Generate mock data for 30 users
for name in names:
    user = User(
        name=name,
        age=fake.random_int(min=18, max=80),
        gender=fake.random_element(elements=('Male', 'Female')),
        weight=fake.random_int(min=50, max=100),
        height=fake.random_int(min=150, max=200)
    )
    # Randomly assign goals to each user
    user.goals.append(choice(goal_records))
    session.add(user)

# Commit to save users and get their IDs
session.commit()

# Query all users
users = session.query(User).all()

# Generate mock data for workouts, nutrition, sleep, wellbeing, and health metrics
for user in users:
    user_id = user.id

    # Generate workouts
    for _ in range(randint(5, 10)):  # Each user gets 5 to 10 workout records
        workout = Workout(
            user_id=user_id,
            workout_type_id=randint(1, len(workout_types)),
            duration=randint(10, 120),
            intensity=fake.random_element(elements=('Low', 'Medium', 'High')),
            calories_burned=randint(100, 1000)
        )
        session.add(workout)

    # Generate nutrition logs
    for _ in range(randint(5, 10)):  # Each user gets 5 to 10 nutrition records
        nutrition = Nutrition(
            user_id=user_id,
            calorie_intake=randint(500, 3000),
            protein=randint(10, 200),
            carbs=randint(10, 300),
            fats=randint(10, 100),
            micronutrients=fake.sentence(nb_words=5)
        )
        session.add(nutrition)

    # Generate sleep logs
    for _ in range(randint(5, 10)):  # Each user gets 5 to 10 sleep records
        sleep = Sleep(
            user_id=user_id,
            total_sleep_time=randint(4, 12),
            light_sleep=randint(1, 6),
            deep_sleep=randint(1, 6),
            REM_sleep=randint(1, 6)
        )
        session.add(sleep)

    # Generate wellbeing logs
    for _ in range(randint(5, 10)):  # Each user gets 5 to 10 wellbeing records
        wellbeing = Wellbeing(
            user_id=user_id,
            meditation_duration=randint(5, 60),
            breathing_practice_frequency=randint(1, 7)
        )
        session.add(wellbeing)

    # Generate health metrics logs
    for _ in range(randint(5, 10)):  # Each user gets 5 to 10 health metric records
        health_metric = HealthMetric(
            user_id=user_id,
            body_fat_percentage=randint(10, 30),
            heart_rate=randint(60, 100),
            blood_pressure=randint(80, 120)
        )
        session.add(health_metric)

# Commit the session to insert the mock data
session.commit()
