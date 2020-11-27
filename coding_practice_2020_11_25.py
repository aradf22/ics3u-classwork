Python Workbook questions: https://repl.it/@AradFarrahi/class#main.py
    # WB 36
 letter = input("Enter a letter here: ")
 if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
   print("Your letter is a vowel!")
 elif letter == "y":
   print("Your letter is sometimes a vowel, sometimes a consonant!")
 else: print("Your letter is a consonant!")


 WB 38
 days = 31
 month = input("Enter the desired month here: ".lower())
 if month == "april" or month == "june" or month == "september" or month == "november":
   days = 30
   print(f"{month} has {days} days")
 elif month == "february":
   days = "28 or 29"
   print(f"{month} has {days} days!")
 if month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
   days = 31
   print(f"{month} has {days} days")
 else:print("Invalid Input")

# WB 40
 side_a = float(input("Enter the first side length of the triangle here: "))
 side_b = float(input("Enter the second side length of the triangle here: "))
 side_c = float(input("Enter the third side length of the triangle here: "))
 if side_a == side_b == side_c:
   print("Your triangle is equilateral!")
 elif side_a == side_b != side_c or side_a == side_c != side_b or side_b == side_c != side_a:
   print("Your triangle is isosceles!")
 else: print("Your triangle is scalene!")

# WB 44
 months = ["january, july, december"]
 choice = input("Enter the month here: ".lower())
 day = input("Enter the day here: ")
 if choice == "january" and day == "1":
   print("That is new year's day!")
 elif choice == "july" and day == "1":
   print("That is Canada Day!")
 elif choice == "december" and day == "25":
   print("That is Christmas day!")
 elif input not in months:
   print("That is not a fixed holiday :/") 
 else: print("Invalid Input")


# WB 46
 month = str(input("Enter the month here: ".lower()))
 day = int(input("Enter the day here: "))
 season = "Winter"
 if month == "january" or month == "february" or month == "march" and day < 20:
   season = "Winter"
 elif month == "march" and day > 20:
   season = "Spring"
 elif month == "april" or month == "may" or month == "june" and day <21:
   season = "Spring"
 elif month == "june" and day > 21:
   season = "Summer"
 elif month == "july" or month == "august" or month == "september" and day < 22:
   season = "Summer"
 elif month == "september" and day > 22:
   season = "Fall"
 elif month == "october" or month == "november" or month == "december" and day < 21:
   season = "Fall"
 elif month == "december" and day > 21:
   season = "Winter"
 print(f"Based on what you entered, the season that day is {season}")

# WB 51
 n_grade = 0
 l_grade = input("Enter the letter grade here: ".upper())
 if l_grade == "A+" or l_grade ==  "A":
   n_grade = 4.0
   print(f"If your letter grade is {l_grade}, your grade point will be {n_grade}!")
 elif l_grade == "A-":
   n_grade = 3.7
   print(f"If your letter grade is {l_grade}, your grade point will be {n_grade}!")
 elif l_grade == "B+":
   n_grade = 3.3
   print(f"If your letter grade is {l_grade}, your grade point will be {n_grade}!")
 elif l_grade == "B":
   n_grade = 3.0
   print(f"If your letter grade is {l_grade}, your grade point will be {n_grade}!")
 elif l_grade == "B-":
   n_grade = 2.7
   print(f"If your letter grade is {l_grade}, your grade point will be {n_grade}!")
 elif l_grade == "C+":
   n_grade = 2.3
   print(f"If your letter grade is {l_grade}, your grade point will be {n_grade}!")
 elif l_grade == "C":
   n_grade = 2.0
   print(f"If your letter grade is {l_grade}, your grade point will be {n_grade}!")
 elif l_grade == "C-":
   n_grade = 1.7
   print(f"If your letter grade is {l_grade}, your grade point will be {n_grade}!")
 elif l_grade == "D+":
   n_grade = 1.3
   print(f"If your letter grade is {l_grade}, your grade point will be {n_grade}!")
 elif l_grade == "D":
   n_grade = 1.0
   print(f"If your letter grade is {l_grade}, your grade point will be {n_grade}!")
 elif l_grade == "F":
   n_grade = 0
   print(f"If your letter grade is {l_grade}, your grade point will be {n_grade}!")
 else: print("Invalid Grade")
  
# WB 52
gpa = float(input("Enter your grade point here: ")) 
 l_grade = str = "A" 
 if gpa == 4.0 or gpa == 4:
   l_grade = "A+"
   print(f"If your grade point is {gpa}, then your letter grade will be {l_grade}")
 elif gpa == 3.7:
   l_grade = "A-"
   print(f"If your grade point is {gpa}, then your letter grade will be {l_grade}")
 elif gpa == 3.3:
   l_grade = "B+"
   print(f"If your grade point is {gpa}, then your letter grade will be {l_grade}")
 elif gpa == 3.0 or gpa == 3:
   l_grade = "B"
   print(f"If your grade point is {gpa}, then your letter grade will be {l_grade}")
 elif gpa == 2.7:
   l_grade = "B-"
   print(f"If your grade point is {gpa}, then your letter grade will be {l_grade}")
 elif gpa == 2.3:
   l_grade = "C+"
   print(f"If your grade point is {gpa}, then your letter grade will be {l_grade}")
 elif gpa == 2.0 or gpa == 2:
   l_grade = "C"
   print(f"If your grade point is {gpa}, then your letter grade will be {l_grade}")
 elif gpa == 1.7:
   l_grade = "C-"
   print(f"If your grade point is {gpa}, then your letter grade will be {l_grade}")
 elif gpa == 1.3:
   l_grade = "D+"
   print(f"If your grade point is {gpa}, then your letter grade will be {l_grade}")
 elif gpa == 1.0 or gpa == 1:
   l_grade = "D"
   print(f"If your grade point is {gpa}, then your letter grade will be {l_grade}")
 elif gpa == 0:
   l_grade = "F"
   print(f"If your grade point is {gpa}, then your letter grade will be {l_grade}")
 else: print("Invalid Grade Point was entered.")

# WB 53
 rating = float(input("Enter the employee rating here: ")) 
 s_raise = rating * 2400.00
 if rating == 0.0:
   print("This employee's performance is unacceptable!")
   print(f"raise = ${s_raise}")
 elif rating == 0.4:
   print("This employee's performance is acceptable!")
   print(f"raise = ${s_raise}")
 elif rating >= 0.6:
   print("This employee's performance is meritorious!")
   print(f"raise = ${s_raise}")
 else: print("Invalid Rating")
  
# WB 57
 year = int(input("Enter a year here: ")) 
 if year % 400 == 0:
   print(f"{year} is a leap year!")
 elif year % 100 == 0:
   print(f"{year} is not a leap year!")
 elif year % 4 == 0:
   print(f"{year} is a leap year!") 
 else: print("This is not a leap year")

 # WB 59
 plate = input("Enter the liscense plate here: " .upper())
 if len(plate) == 7 and plate[0:3] >= "0" and plate[3:6] >= "A":
   print("This is a valid new license plate")
 elif len(plate) == 6 and plate[0:2] >= "A" and plate [2:5] >= "0":
   print("This is a valid older liscence plate")
 else: print("Invalid Plate")

  
  
  Codingbat questions: https://repl.it/@AradFarrahi/coding-bat#main.py 
      
  # CB Hello name
def hello_name(name):
  return "Hello " + (name) + "!"

# CB abba
def make_abba(a, b):  
  return a + b + b + a
  
# CB Last 2
def last_two(string: str) -> str: 
    if len(string) < 2:
      return string
    else:
      last_char = string[-1]
      second_last_char = string[-2]
      end = string[0:-2]
      return end + last_char + second_last_char
result = last_two('coding')
print(result)

# CB First 2
def first_two(str): 
  if len(str) < 2:
    return str
  else:
    first_char = str[0]
    second_char = str[1]
    new_word = first_char + second_char
    return new_word  

# CB Extra end
def extra_end(str):
  if len(str) < 2:
    return str + str + str
  else:
    last_char = str[-1]
    second_last = str[-2]
    return second_last + last_char + second_last + last_char + second_last + last_char

# CB Without end
def without_end(str):
  if len(str) < 2:
    return " "
  else:
    return str[1:-1]

# CB Left 2
def left2(str):
  if len(str) < 2:
    return str
  else:
    return (str)[2:] + str[0:2]

# CB combo string
def combo_string(a, b):
  if len(a) < len(b):
    return a + b + a
  elif len(b) < len(a):
    return b + a + b

# CB First half
def first_half(str): 
  return str[0:len(str)/2]
CB Non Start
def non_start(a, b): 
  return a[1:] + b[1:]

# CB make out word
def make_out_word(out, word): 
  return out[0:2] + word + out[2:]





