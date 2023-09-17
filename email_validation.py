#-------------------------Email Validation--------------------------------------
email = input("Enter your Email-id :") # e@g.in
k,l,m=0,0,0
if len(email)>=6:    # 1 condition                       # len(email) function use for email length and '>=' means greater than 6 or equal to 6
    if email[0].isalpha(): # 2 condition                 # email[0] means email first chaaracter is isalpha() 'only alphabet not numeric'
        if ('@' in email) and (email.count("@")==1): #3  # @ in email or not and count ==1 not more than 1
            if(email[-4]==".") ^(email[-3]=="."):    #4  # Two Types of Index Number 1--> Positive Index Number 2--> Negative Index Number
                for i in email:                          # Positive Index : Left to Right Move | Negative Index : Right to Left Move
                    if i ==i.isspace(): # 5 condition    check space in email
                        k=1
                    elif i.isalpha():   # 5             check alphanumeric or not
                        if i==i.upper():                 # upper case not accepted
                            l=1
                    elif i.isdigit():   # 5              check digit than continue'
                        continue
                    elif i=='_' or i=="." or i=="@": # 5
                        continue
                    else:
                        m=1
                if k==1 or l==1 or m==1:
                    print('Wrong email use proper format of email : 5')
            else:
                print('Wrong email use . in place : 4')
        else:
            print('Wrong email use @ one time only : 3')
    else:
        print('Wrong email only alphabet use  :2')
else:
    print('Wrong email length not correct :1')