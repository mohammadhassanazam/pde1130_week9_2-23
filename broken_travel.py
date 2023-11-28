# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? "))
                   #here above input was not closed from left so i added ( , deleted fullstop after int , the string was also not closed single quotation mark ' so i changed to double quotation mark and at last also deleted one = from two == username-mohammadhassanazam (mohammadhassanazam@gmail.com)

if year <= 1900: #here added : after 1900 user.name-mohammadhassanazam (mohammadhassanazam@gmail.com)
    print ("Woah, that's the past!")
           #above changed both single quotation mark to double quotation username-mohammadhassanazam (mohammadhassanazam@gmail.com)
elif year > 1900 and year < 2020: #here i deleted && to and user.name-mohammadhassanazam (mohammadhassanazam@gmail.com)
    print ("That's totally the present!")
else: #here i changed elif to else username- mohammadhassanazam (mohammadhassanazam@gmail.com)
    print ("Far out, that's the future!!")
