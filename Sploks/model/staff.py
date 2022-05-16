from model import mold


class Staff:

    def load(self, id):
        staff_member = mold.selectOneWithParams("*", "staffs", f"Where id = {id}")

        self.id = staff_member['id']
        self.firstname = staff_member['firstname']
        self.lastname = staff_member['lastname']
        self.phone = staff_member['phone']

    def update(self, values):

            mold.updateOne("staffs", "phone", f"{values}", f"WHERE id = {self.id}")



    @staticmethod
    def all():
        return mold.selectWithParams("*", "staffs")
