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

if re.search("..*@.*", email):
    print("Valid")
else:
  print("Invalid")    