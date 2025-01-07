#Braden leach
#January 7 2024
#Return Function Room Calculator
import time

#----1----#
def welcome_user():
    print('Hello this is a calculator to find the area of your room!')
# #----2----#
def user_length():
    length= float(input('Please input the length of your room in feet: '))
    return length

# #----3----#
def user_width():
    width= float(input('Please input the width of your room in inches: '))
    return width

# #----4----#
def calc_area(length,width):
     area = length * width
     return area 

# #----5----#
def display_area(area):
     print(f'The area of your room is {area:.2f} sq. ft.')


#----6----#
def thank_user():
 time.sleep(1)
 print('Thank you for using my calculator!')

#order
def main():
   welcome_user()

   length = user_length()

   width = user_width()

   area = calc_area(length,width)

   display_area(area)

   thank_user()

if __name__ == "__main__":
   main()