import datetime


class Helpers:

    @staticmethod
    def formatDate(date):
        date_sql = '%Y-%m-%d %H:%M:%S'
        date = datetime.datetime.strptime(str(date), date_sql)
        return date.strftime("%d %B %Y")
