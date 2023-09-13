# Python program to check if year is a leap year or not

def checkleafyear(year):
  if year % 400 == 0 and year % 100 == 0:
    print('leaf year')
    return 1
  elif year % 4 ==0 and year % 100!= 0:
    print('leaf year')
  else:
    print("{0} is not a leap year".format(year))
year=int(input("Enter a year:"))
checkleafyear(year)