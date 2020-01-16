# pwndpasswordchecker

# ABOUT
This a safe way to check if your password is present in a leaked database without providing the whole password
To be save you are not sending the complete password hash to the server we break it down into 2 parts:
 - first part will be used to call the website API which will retrieve all hashes starting with the 5 characters from the hash
 - second part will be the rest of the hash used locally by python to search if any of the returned hashes are found

# USAGE
./pwndpasswordchecker.py
Enter password to check: 123456
Password hash: 7c4a8d09ca3762af61e59520943dc26494f8941b
PASSWORD HAS BEEN PWNED!!!
