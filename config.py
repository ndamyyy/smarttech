import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'une_clé_secrète_très_sécurisée'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///smarttech.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  