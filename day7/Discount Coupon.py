#Make a ecom system with 5 products make a coupon code system where we will get discount when apply coupon code
Total= 0
product ={'Cricket Bat':650,'Ball':200,'Cricket Gloves':500,'Pads':300, 'Helmet':250}
discount ={'DIS20':0.20,'DIS25':0.25,'DIS30':0.30}
print('Welcome To Sports Goods Store')
kit= input("please add the required product in kit to do so type 'y'")
while(kit!='n'):
    if kit=='y'or'c'or'b'or'g'or 'p'or 'h' :
        kit= input("Type 'c' for Cricket Bat,'b' for Ball,'g' for Cricket Gloves,'p' for Pads,'h' for Helmet, 'n' for Total Amount:")
        if kit =='c':
         Total = Total + product['Cricket Bat']
        elif kit =='b':
         Total = Total + product['Ball']
        elif kit =='g':
         Total = Total +product['Cricket Gloves']
        elif kit=='p':
         Total = Total +product['Pads']
        elif kit=='h':
         Total = Total +product['Helmet']
    else:
        if kit!='n':
            print("sorry! you have type wrong button")
print("Your Amount is {}".format(Total))
code =input("Do You Have any Coupon Code?(y/n):")
if code=='y':
    coupon=input("Please enter your coupon code:")
    if coupon in discount.keys():
        Total= Total-Total*discount[coupon]
        print("your total amount after applying coupon code is {}".format(Total))
    else:
        print("Sorry! coupon code you entered is invalid")
        print("your total amount is {}".format(Total))
