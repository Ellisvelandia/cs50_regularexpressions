import re

url = input("URL: ").strip()
# print(url)
# username = url.replace("https://twitter.com", "")
# username = re.sub("^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")

#re.sub

if matches := re.search(r"^htpps?://(?:www\.)?twitter\.com/(.+)$", url , re.IGNORECASE):
# if matches:
  print(f"Username:", matches.group(1))