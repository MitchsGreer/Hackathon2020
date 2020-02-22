from classes import User, Picture

def loadUser(id=5):
    # find the user based on the given id
    infile = open("../data/test_users/user_profiles.csv", "r")

    for line in infile:
        items = line.split(",")
        print(items)
        cur_id = int(items[0])
        name = items[1].lstrip()
        gender = items[2].lstrip()
        desired_gender = items[3].lstrip()
        user_pic = Picture(name=items[4].lstrip())

        # NOTE: only works for lists of length 1
        yup = []
        yup.append(items[5].strip()[1:-1])
        nup = []
        nup.append(items[6].strip()[1:-1])

        if cur_id == id:  
            infile.close()  
            ret = User(
                userID=cur_id, name=name,
                gender=gender, desiredGender=desired_gender,
                picture=user_pic, yup=yup, nup=nup)
            print(ret)
            return ret

    infile.close()


if __name__ == "__main__" :
    loadUser()
