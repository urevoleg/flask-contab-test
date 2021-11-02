import os
from pathlib import Path


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or "8b91de6904034b85ce77fa5f2419efaa"
    FILE_PATH_JOB_TEST = os.path.join(str(Path.home()), "Downloads", "flask-cron-job.txt")
