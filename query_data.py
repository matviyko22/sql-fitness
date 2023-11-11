from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from create import User, Workout, Nutrition, Sleep, Wellbeing, HealthMetric, Goal, WorkoutType, user_goals

# Create a SQLAlchemy session
engine = create_engine('sqlite:///app.db')
session = Session(bind=engine)

# Welcome message
print("Welcome to the Fitness Tracker App!")
print("This app provides various health and fitness metrics for users.\n")

# Prompt the user to enter their name
user_name = input("Please enter your name: ")

# Find the user in the database by their name
user = session.query(User).filter(User.name == user_name).first()

# Check if the user exists
if user:
    user_id = user.id
    print(f"\nUser: {user.name}")

    # Query 1: Total calories burned by the user
    total_calories_burned = session.query(func.sum(Workout.calories_burned)).filter(Workout.user_id == user_id).scalar()
    print(f"{user.name} has burned a total of {total_calories_burned} calories.")

    # Query 2: Average calorie intake of the user
    average_calorie_intake = session.query(func.avg(Nutrition.calorie_intake)).filter(Nutrition.user_id == user_id).scalar()
    print(f"{user.name}'s average calorie intake is {round(average_calorie_intake, 0)} calories.")

    # Query 3: Most common workout type for the user
    most_common_workout_type = session.query(WorkoutType.type).join(Workout, WorkoutType.id == Workout.workout_type_id).filter(Workout.user_id == user_id).group_by(WorkoutType.type).order_by(func.count(WorkoutType.type).desc()).first()
    print(f"{user.name}'s most common workout type is {most_common_workout_type[0]}.")

    # Query 4: Average sleep time of the user
    average_sleep_time = session.query(func.avg(Sleep.total_sleep_time)).filter(Sleep.user_id == user_id).scalar()
    print(f"{user.name}'s average sleep time is {average_sleep_time} hours.")

    # Query 5: Users with a specific fitness goal
    user_goal = session.query(Goal.goal).join(user_goals).filter(user_goals.c.user_id == user_id).first()
    users_with_same_goal = session.query(User.name).join(user_goals).join(Goal).filter(Goal.goal == user_goal[0]).all()
    print(f"undefinedsers with the same goal as {user_name}: {[user[0] for user in users_with_same_goal]}")

    # Query 6: Total duration of workouts for the user
    total_workout_duration = session.query(func.sum(Workout.duration)).filter(Workout.user_id == user_id).scalar()
    print(f"{user.name}'s total workout duration is {total_workout_duration} minutes.")

    # Query 7: Average body fat percentage of the user
    average_body_fat_percentage = session.query(func.avg(HealthMetric.body_fat_percentage)).filter(HealthMetric.user_id == user_id).scalar()
    print(f"{user.name}'s average body fat percentage is {average_body_fat_percentage}%.")

    # Query 8: Average heart rate of the user
    average_heart_rate = session.query(func.avg(HealthMetric.heart_rate)).filter(HealthMetric.user_id == user_id).scalar()
    print(f"{user.name}'s average heart rate is {round(average_heart_rate, 0)} bpm.")

    # Query 9: Total meditation duration for the user
    total_meditation_duration = session.query(func.sum(Wellbeing.meditation_duration)).filter(Wellbeing.user_id == user_id).scalar()
    print(f"{user.name}'s total meditation duration is {total_meditation_duration} minutes.")

else:
    print("User not found.")

# Close the session
session.close()
