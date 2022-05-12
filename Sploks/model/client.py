from const import con
from model import mold


class Customer:

    def load(self, id):
        customer_data = mold.selectOneWithParams("SELECT customers.id,firstname,lastname,email,mobile,address,"
                                                 "npas.npa,npas.town",
                                                 "customers",
                                                 f"inner join npas on npas.id = customers.npa_id Where id = {id}")
        self.id = customer_data['id']
        self.lastname = customer_data['lastname']
        self.firstname = customer_data['firstname']
        self.email = customer_data['email']
        self.mobile = customer_data['mobile']
        self.address = customer_data['address']
        self.npa = customer_data['npa']
        self.town = customer_data['town']

    @staticmethod
    def all():
        return mold.selectWithParams("customers.id,lastname,firstname,address,npas.npa,npas.town,email,mobile",
                                     "customers", "inner join npas on npas.id = customers.npa_id")
