from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Association table for the many-to-many relationship between Users and Goals
user_goals = Table('user_goals', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('goal_id', Integer, ForeignKey('goals.id'))
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    weight = Column(Float)
    height = Column(Float)
    workouts = relationship('Workout', backref='user')
    nutrition_logs = relationship('Nutrition', backref='user')
    sleep_logs = relationship('Sleep', backref='user')
    wellbeing_logs = relationship('Wellbeing', backref='user')
    health_metrics = relationship('HealthMetric', backref='user')
    goals = relationship('Goal', secondary=user_goals, backref='users')

class Goal(Base):
    __tablename__ = 'goals'
    id = Column(Integer, primary_key=True)
    description = Column(String)

class Workout(Base):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    workout_type_id = Column(Integer, ForeignKey('workout_types.id'))
    duration = Column(Integer)
    intensity = Column(String)
    calories_burned = Column(Integer)

class WorkoutType(Base):
    __tablename__ = 'workout_types'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    workouts = relationship('Workout', backref='workout_type')

class Nutrition(Base):
    __tablename__ = 'nutrition'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    calorie_intake = Column(Integer)
    protein = Column(Integer)
    carbs = Column(Integer)
    fats = Column(Integer)
    micronutrients = Column(String)

class Sleep(Base):
    __tablename__ = 'sleep'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    total_sleep_time = Column(Integer)
    light_sleep = Column(Integer)
    deep_sleep = Column(Integer)
    REM_sleep = Column(Integer)

class Wellbeing(Base):
    __tablename__ = 'wellbeing'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    meditation_duration = Column(Integer)
    breathing_practice_frequency = Column(Integer)

class HealthMetric(Base):
    __tablename__ = 'health_metrics'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    body_fat_percentage = Column(Float)
    heart_rate = Column(Integer)
    blood_pressure = Column(Integer)
