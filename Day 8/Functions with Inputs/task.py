
def life_in_weeks(age):
  age=int(input("Enter your age: "))
  weeks_left=(90-age)*52
  print('You have '+str(weeks_left)+ ' weeks left.')


# Call your function with hard coded values
life_in_weeks(12)