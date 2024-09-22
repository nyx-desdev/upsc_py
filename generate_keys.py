import pickle
from pathlib import Path

import streamlit_authenticator as stauth

# Define user data
names = ["Nikhil Arya", "Vaibhav Gupta"]
usernames = ["nyxdesdev", "vaibhu"]  # Use usernames instead of usersnames
passwords = ["XXXX", "XXXX"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)