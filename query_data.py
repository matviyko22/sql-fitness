from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from create import User, Workout, Nutrition, Sleep, Wellbeing, HealthMetric, Goal, WorkoutType, user_goals

# Create a SQLAlchemy session
engine = create_engine('sqlite:///app.db')
session = Session(bind=engine)

# Query 1: Total calories burned by a specific user
user_id = 1
total_calories_burned = session.query(func.sum(Workout.calories_burned)).filter(Workout.user_id == user_id).scalar()
print(f"Total calories burned by user {user_id}: {total_calories_burned}")

# Query 2: Average calorie intake of a specific user
average_calorie_intake = session.query(func.avg(Nutrition.calorie_intake)).filter(Nutrition.user_id == user_id).scalar()
print(f"Average calorie intake of user {user_id}: {average_calorie_intake}")

# Query 3: Most common workout type for a specific user
most_common_workout_type = session.query(WorkoutType.type).filter(Workout.user_id == user_id).group_by(WorkoutType.type).order_by(func.count(WorkoutType.type).desc()).first()
print(f"Most common workout type for user {user_id}: {most_common_workout_type[0]}")

# Query 4: Average sleep time of a specific user
average_sleep_time = session.query(func.avg(Sleep.total_sleep_time)).filter(Sleep.user_id == user_id).scalar()
print(f"Average sleep time of user {user_id}: {average_sleep_time}")

# Query 5: Users who have a specific fitness goal
goal_description = 'Lose weight'
users_with_goal = session.query(User.name).join(user_goals).join(Goal).filter(Goal.description == goal_description).all()
print(f"Users with the goal '{goal_description}': {[user[0] for user in users_with_goal]}")

# Query 6: Total duration of workouts for a specific user
total_workout_duration = session.query(func.sum(Workout.duration)).filter(Workout.user_id == user_id).scalar()
print(f"Total workout duration for user {user_id}: {total_workout_duration}")

# Query 7: Average body fat percentage of a specific user
average_body_fat_percentage = session.query(func.avg(HealthMetric.body_fat_percentage)).filter(HealthMetric.user_id == user_id).scalar()
print(f"Average body fat percentage of user {user_id}: {average_body_fat_percentage}")

# Query 8: Average heart rate of a specific user
average_heart_rate = session.query(func.avg(HealthMetric.heart_rate)).filter(HealthMetric.user_id == user_id).scalar()
print(f"Average heart rate of user {user_id}: {average_heart_rate}")

# Query 9: Total meditation duration for a specific user
total_meditation_duration = session.query(func.sum(Wellbeing.meditation_duration)).filter(Wellbeing.user_id == user_id).scalar()
print(f"Total meditation duration for user {user_id}: {total_meditation_duration}")

# Query 10: Users with the highest total calories burned
top_calorie_burners = session.query(User.name, func.sum(Workout.calories_burned)).group_by(User.name).order_by(func.sum(Workout.calories_burned).desc()).all()
print("Users with the highest total calories burned:")
for user in top_calorie_burners:
    print(f"{user[0]}: {user[1]}")

# Query 11: Users with the highest average sleep time
top_sleepers = session.query(User.name, func.avg(Sleep.total_sleep_time)).group_by(User.name).order_by(func.avg(Sleep.total_sleep_time).desc()).all()
print("Users with the highest average sleep time:")
for user in top_sleepers:
    print(f"{user[0]}: {user[1]}")

# Close the session
session.close()