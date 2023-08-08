url = input("URL: ").strip()
print(url)

# username = url.replace("https://twitter.com", "")
username = re.sub("^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

#re.sub

