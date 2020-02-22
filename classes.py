from PIL import Image


class Picture:
    def __init__(self, name="Picture Name", image=""):
        self.name = name
        self.picture = image

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.name)


class User:

    def __init__(self, userID=-1, name="User Name", gender=None, desiredGender=None, picture=Picture(), yup=[Picture()], nup=[Picture()], foundYou=[], matched=[]):
        self.userID = userID
        self.name = name
        self.gender = gender
        self.desiredGender = desiredGender
        self.picture = picture
        self.yup = yup
        self.nup = nup
        self.foundYou = foundYou
        self.matched = matched

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        out_string = (
            str(self.name)
            + ":\n\tUser ID: "
            + str(self.userID)
            + "\n\tGender: "
            + str(self.gender)
            + "\n\tDesired Gender: "
            + str(self.desiredGender)
            + "\n\tPicture: "
            + str(self.picture)
            + "\n\tYup List: "
        )

        for item in self.yup:
            out_string += str(item) + ", "

        out_string += "\n\tNup List: "

        for item in self.nup:
            out_string += str(item) + ", "

        out_string += "\n\tMatched List: "

        for item in self.matched:
            out_string += str(item) + ", "

        out_string += "\n\tFound You Lists: "

        for item in self.foundYou:
            out_string += str(item) + ", "

        return out_string
