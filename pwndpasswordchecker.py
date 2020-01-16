import hashlib
import urllib.request
import urllib.parse
from getpass import getpass

# enter the desired password and create the SHA1 password hash
mystring = getpass()
hash_obj = hashlib.sha1(mystring.encode())
hash_string = hash_obj.hexdigest()

# to be safe you are not sending the complete password hash to the server we break it down into 2 parts
# search_range will be used to call the website API which will retrieve all hashes starting with the 4 characters
# search_value will be used locally by python to search if any of the returned hashes are the one for the password
search_range = hash_string[:5].upper()
search_value = hash_string[-35:].upper()

# call pwnedpasswords.com API with the range hash
url = "https://api.pwnedpasswords.com/range/" + search_range
search_result = urllib.request.urlopen(url).read().decode("utf-8")

# check the search_results from the API contain the input password hash
if search_result.find(search_value) > -1:
    print("PASSWORD HAS BEEN PWNED!!!")
    print('Password hash: ' + hash_string)
else:
    print("PASSWORD IS STILL SAFE")
