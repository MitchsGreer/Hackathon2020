

class User:

    def __init__(self, userID=-1, name="No Name", gender=None, desired_gender=None, picture={"name": "", "picture": ""}, yup=[], nup=[]):
        self.userID = userID
        self.name = name
        self.gender = gender
        self.desired_gender = desired_gender
        self.picture = picture
        self.yup = yup
        self.nup = nup

    def __str__(self):

        out_string = (
            str(self.name)
            + ":\n\tUser ID: "
            + str(self.userID)
            + "\n\tGender: "
            + str(self.gender)
            + "\n\tDesired Gender: "
            + str(self.desired_gender)
            + "\n\tPicture: "
            + str(self.picture["name"])
            + "\n\tYup List: "
        )

        for item in self.yup:
            out_string += "\t"
            out_string += item["name"] + ", "

        out_string += "\n\tNup List: "

        for item in self.nup:
            out_string += "\t"
            out_string += item["name"] + ", "

        return out_string

    def __rpr__(self):
        pass


new_user = User()
print(new_user)
