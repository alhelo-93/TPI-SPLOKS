import datetime


class Helpers:

    @staticmethod
    def formatDate(date):
        date_sql = '%Y-%m-%d %H:%M:%S'
        date = datetime.datetime.strptime(str(date), date_sql)
        return date.strftime("%d %B %Y")

    @staticmethod
    # returns the id of the npa passed. It has been either found or created in the database
    def findOrCreateNPA(npa, town):
        """
        # Hypothèse: le npa existe déjà
        # id = select from npas where npa_field = npa
        # if id == null
        # id = lastinsertid après insert into npas (npa, town) values (paramètres)
        # return id
        """