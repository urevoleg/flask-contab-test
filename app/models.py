import datetime as dt

from flask_restful import Resource


class Time(Resource):
    def get(self):
        return {'time': dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
