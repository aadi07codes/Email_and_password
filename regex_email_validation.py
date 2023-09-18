#-----------------Email validation use Regex module-----------------------------
import re               #------------import re--- regex module
email = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$" #----condition through Regex '^' syntex means starting
user_email = input("Enter Your Email ID..:")       #----^[a-z] means first character start with alphabet
if re.search(email,user_email):                    # + sign means in Regex is join and \ when we search character through Regex use '\'
    print("Right Email Id....")                    # [\._]? --->'?' question mark means dot and underscore use only one time and \
else:                                              # \w means search string in Regex and {2,3} and search right to left
    print("Wrong Email Id....")

