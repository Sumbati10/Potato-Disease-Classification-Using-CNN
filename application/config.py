import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    MODEL = os.path.join(BASE_DIR, 'static', 'models', 'model_v1.h5')
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Maximum file size: 16MB
