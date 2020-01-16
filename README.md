# pwndpasswordchecker

# ABOUT
This a safe way to check if your password is present in a leaked database without providing the whole password.

To be safe you are not sending the complete password hash to the server we break it down into 2 parts:
 - first part will be used to call the haveibeenpwned.com API which will retrieve all hashes starting with the 5 characters from our hash
 - second part will be the rest of the hash, used locally by python, to check if it's found within the hashes returned by the API

# USAGE
```console
./pwndpasswordchecker.py
Enter password to check: 123456
Password hash: 7c4a8d09ca3762af61e59520943dc26494f8941b
PASSWORD HAS BEEN PWNED!!!
```

# DISCLAIMER
Users are asked to input their password durring the runtime of this script. The owner does not take any responsability of any theft/lost of your data. This script does not store the input data. 
Please first check the code and never trust anybody with your credentials.
