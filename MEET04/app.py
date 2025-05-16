from werkzeug.security import generate_password_hash, check_password_hash

password = generate_password_hash("qwerty")
print(password)

check = check_password_hash(password, "qwerty")
print(check)