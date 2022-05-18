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
        self.npaID = customer_data['npa_id']
        self.npa = customer_data['npa']
        self.town = customer_data['town']

    def createNew(self, values):
            columus = 'lastname,firstname,address,email,mobile,npa_id'
            new_id = mold.createOne("customers", f"{columus}", f"{values}")
            self.id = new_id

    def updateOne(self, values):
        mold.updateOne("customers",
                       f"lastname='{values[0]}',firstname='{values[1]}',address='{values[2]}',email='{values[3]}', "
                       f"mobile= '{values[4]}'",
                       f"WHERE id = {self.id}")

    @staticmethod
    def all():
        return mold.selectWithParams("customers.id,lastname,firstname,address,npas.npa,npas.town,email,mobile",
                                     "customers", "inner join npas on npas.id = customers.npa_id order by lastname")
