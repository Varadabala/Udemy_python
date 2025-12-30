credit_score = int(input("Enter credit score : "))
if credit_score < 400 and credit_score > 850:
    print('Invlid credit score')
else:
    if(credit_score >= 400 and credit_score < 600):
        print("Silver Card")
    elif(credit_score >= 600 and credit_score < 800):
        print("Gold Card")
    else:
        print("Platinum Card")            

"""
o/p: 

Enter credit score : 400
Silver Card

Enter credit score : 850
Platinum Card
"""        