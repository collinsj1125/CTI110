# Areas of Rectangles
# 02/12/2019
#CTI-110-reas of Rectangles
#Justin Collins

# Get the dimensions of rectangle 1

length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

# Get the dimensions of rectangle 2

length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

# Calculate which has the greater area

area1 = length1 * width1
area2 = length2 * width2

# Determine which has the greater area

if area1 > area2:
    print ('Reactangle 1 has a greater area. ')

elif area2 > area1:
    print ('Rectangle 2 has a greater area. ')

else:
    print ('Both have the same area. ')
