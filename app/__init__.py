from flask import Flask
from flask_crontab import Crontab
from flask_restful import Api
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
crontab = Crontab(app)


from app import routes, jobs, models


@crontab.job(minute="*")
def my_scheduled_job():
    jobs.do_something(path=Config.FILE_PATH_JOB_TEST)


@crontab.job(minute="50")
def my_scheduled_job_2():
    jobs.do_once()
