import re

email = input("whats your email? ").strip()

# if "@" in email:
#   print("valid")
# else:
# #     print("Inavalid")
# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#   print("Invalid")    

# if re.search(r"^\w+@\w+\.(com|edu|net|org)$", email, re.IGNORECASE ):
# if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE ):
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE ):
    print("Valid")
else:
  print("Invalid")    

#  \d decimal digit 
#  .  
#  *  
#  +  
#  ?  
