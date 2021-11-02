from flask import Flask
from flask_crontab import Crontab
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
crontab = Crontab(app)


from app import routes, jobs


@crontab.job(minute="*")
def my_scheduled_job():
    jobs.do_something(path=Config.FILE_PATH_JOB_TEST)


@crontab.job(minute="45")
def my_scheduled_job_2():
    jobs.to_tlg()
