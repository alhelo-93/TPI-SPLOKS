from model import mold
from model.helpers import Helpers


class Contract:

    def load(self, id):
        """
            < load >: This function is used to set attributes to an objet.
            < self >: Gives access to the attributes and methods of the class. Example: self.id, self.save(...)
            < id >: This param is used to get the load the right contract. Type: not defined. Can be a string or an int.
            return: This function does not return anything
        """
        data = mold.selectWithParamsgroupby(
            "contracts.id , customers.firstname , customers.lastname,"
            "count(renteditems.id) as NBarticles, contracts.creationdate , contracts.effectivereturn, "
            "contracts.plannedreturn ",
            "contracts",
            "inner join renteditems on contract_id=contracts.id "
            f"INNER join customers ON customers.id = contracts.customer_id WHERE contrats.id = {id}")
        creation_date = Helpers.formatDate(data['creationdate'])
        return_date = Helpers.formatDate(data['effectivereturn'])
        planedreturn_date = Helpers.formatDate(data['plannedreturn'])



        self.id = data['id']
        self.firstname = data['firstname']
        self.lastname = data['lastname']
        self.NBarticles=data['NBarticles']
        self.creation_date = creation_date
        self.effective_return = return_date




    @staticmethod
    def all():
        return mold.selectWithParamsgroupby(
            "contracts.id , customers.firstname , customers.lastname, count(renteditems.id) as NBarticles,"
            "contracts.creationdate , "
            "contracts.plannedreturn",
            "contracts", "inner join renteditems on contract_id=contracts.id "
            "INNER join customers ON customers.id = contracts.customer_id")
