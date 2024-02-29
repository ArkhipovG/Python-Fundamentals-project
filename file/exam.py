from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------
# Define the possible characters
possible_chars = 'abcdefghijklmnopqrstuvwxyz'

# Brute force to find the missing letters
for char1 in possible_chars:
    for char2 in possible_chars:
        secret_password = char1 + char2 + 'bcmpda'

        # Try to unzip with the current password
        if unzip_with_7z(zip_file_path, dest_path, password=secret_password):
            print(f"Password found: {secret_password}")
            exit()  # Stop after finding the correct password

print("Password not found.")