from app.modules.auth.jwt_handler import create_access_token

token = create_access_token(
    {
        "sub": "adiveppa@example.com",
        "role": "job_seeker",
    }
)

print(token)