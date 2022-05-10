# Duran Ramlall 
# Learn Python - String Formatting
# Friday May 6 2022 
# TEJ4M1 P2

# String Formatting
# In order to use variables within a string the % is used
# There are different specifiers 
# %s    | String 
# %d    | Integers
# %f    | Float values
# %.f   | Float values (fixed digit)
# %x/%X | Integers in hex representation
# In order to call that set of data use %(dataset)
data = ("Duran", "Ramlall", 25.6)
formattedString = "Hello %s %s. Your phone currently has %.1f%% battery left"
print(formattedString %(data))

# Note, in order to use the % sign to represent the percent I used %%