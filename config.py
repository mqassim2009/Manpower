import os

class Config:
    """Configuration settings for the Qatar Manpower application"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///manpower.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
