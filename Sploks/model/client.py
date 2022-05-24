from const import con
from model import mold


class Customer:

    def load(self, id):
        customer_data = mold.selectOneWithParams("customers.id,firstname,lastname,email,mobile,address,npa_id,"
                                                 "npas.npa,npas.town",
                                                 "customers",
                                                 f"inner join npas on npas.id = customers.npa_id Where customers.id = {id}")
        self.id = customer_data['id']
        self.lastname = customer_data['lastname']
        self.firstname = customer_data['firstname']
        self.email = customer_data['email']
        self.mobile = customer_data['mobile']
        self.address = customer_data['address']
        self.npa = customer_data['npa']
        self.town = customer_data['town']

    def loadHistory(self, id):
            history_data = mold.selectOneWithParams("timestamp,text", 'logs',
                                        "inner join customers on customers.id = logs.customer_id"
                                        "Where logs.customer_id= {id}")
            self.id = history_data['id']
            self.lastname = history_data['customer_id']
            self.firstname = history_data['firstname']


    def createNew(self, values):
        columus = (['npa', 'town', 'firstname', 'lastname', 'address', 'email', 'mobile', 'npa_id'])

        new_id = mold.createOne("npas", f"({columus[0]},{columus[1]} )", f"({values[0]},'{values[1]}');"
                                                                         f"SET @last_id_in_npas = LAST_INSERT_ID();"
                                                                         f"INSERT INTO customers ({columus[2]},{columus[3]},{columus[4]},{columus[5]},{columus[6]},{columus[7]})"
                                                                         f"VALUES ('{values[2]}', '{values[3]}', '{values[4]}', '{values[5]}', '{values[6]}', @last_id_in_npas);")
        self.id = new_id

    def updateOne(self, values):
        mold.updateOne("customers ", "npas on npas.id = customers.npa_id",
                       f"firstname='{values[0]}',lastname='{values[1]}',address='{values[2]}',email='{values[3]}',"
                       f"mobile= '{values[4]}', npa= {values[5]} ,town= '{values[6]}'",
                       f"WHERE customers.id = {self.id} ")


    @staticmethod
    def all():
        return mold.selectWithParams("customers.id,lastname,firstname,address,npas.npa,npas.town,email,mobile",
                                     "customers", "inner join npas on npas.id = customers.npa_id order by lastname")

    @staticmethod
    def Historylist():
        return mold.selectWithParams("timestamp,text", 'logs',
                                        "inner join customers on customers.id = logs.customer_id")

