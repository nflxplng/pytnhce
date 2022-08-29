# Python3 code to demonstrate each occurrence frequency using naive method 
# Initializing string 
test_str = "New Horizon College of Engineering"
# Using naive method to get count of each element in string 
all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
  
# Printing result 
print ("Count of all characters is:\n "  +  str(all_freq))
