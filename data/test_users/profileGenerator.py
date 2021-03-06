# This is a script for generating a list of random profiles
# in "user_profiles.csv"

import random

infile = open("auto_names.csv", "r")
outfile = open("user_profiles.csv", "w")

for i in range(100):
    line = str(i) + ", "    # add userID

    temp = infile.readline().rstrip()

    line += temp + " "  # add name & gender

    # pick a random gender preference
    if random.randint(0,1) == 1:
        line += "M, " # choose male
    else:
        line += "F, "# choose female

    # pick a random picture (based on person's gender)
    gender = temp[1].lstrip()

    if gender == "M":
        line += "male" + str(random.randint(1,9)) + ".jpg, " # M
    else:
        line += "female" + str(random.randint(1,9)) + ".jpg, "# F or None

    # add yup
    if gender == "M":
        line += "[female" + str(random.randint(1,9)) + ".jpg], "
    else:
        line += "[male" + str(random.randint(1,9)) + ".jpg], "

    # add nup
    if gender == "M":
        line += "[female" + str(random.randint(1,9)) + ".jpg], "
    else:
        line += "[male" + str(random.randint(1,9)) + ".jpg]"

    line += "\n"
    outfile.write(line);

infile.close()
outfile.close()
