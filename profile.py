

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

    # loads this profile from a given json file
    # def loadFromCSV(self, filename="user_profiles.csv"):
    #     file = open(filename, "r")
    #     file.close()

    # append this profile as a csv file.
    def saveToCSV(self, filename="user_profiles.csv"):
        file = open(filename, "a");

        # file format is: 
        # userID, name, gender, desired_gender, picture, yup, nup
        result = str(self.userID)
        result += ", " + str(self.name)
        result += ", " + str(self.gender)
        result += ", " + str(self.desired_gender)
        result += ", " + str(self.picture)
        result += ", " + str(self.yup)
        result += ", " + str(self.nup) + "\n"

        file.write(result);
        file.close()

new_user = User()
print(new_user)


new_user.saveToCSV()
