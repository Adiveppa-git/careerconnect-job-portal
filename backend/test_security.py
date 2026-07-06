from app.utils.security import hash_password, verify_password

password = "Seeker@1"

hashed = hash_password(password)

print("Original:", password)
print("Hashed :", hashed)

print(
    "Verify:",
    verify_password(password, hashed),
)