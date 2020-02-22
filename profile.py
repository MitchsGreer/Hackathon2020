

class User:

    def __init__(userID=-1, name="", gender=None, desired_gender=None, picture="", yup=[], nup=[]):
        self.userID = userID
        self.name = name
        self.gender = gender
        self.desired_gender = desired_gender
        self.picture = picture
        self.yup = yup
        self.nup = nup

    def __str__(self):
        pass

    def __rpr__(self):
        pass
