import secrets
import string

def generate_secret_key(length=50):
    """Generate a secure random secret key"""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def generate_jwt_secret_key(length=32):
    """Generate a secure JWT secret key (256-bit)"""
    return secrets.token_hex(length)  # 32 bytes = 64 hex characters

if __name__ == "__main__":
    print("Generating secure secret keys...")
    print()

    django_secret = generate_secret_key()
    jwt_secret = generate_jwt_secret_key()

    print("DJANGO_SECRET_KEY=" + django_secret)
    print("JWT_SECRET_KEY=" + jwt_secret)
    print()

    print("Copy these values to your .env file:")
    print("===================================")
    print(f"DJANGO_SECRET_KEY={django_secret}")
    print(f"JWT_SECRET_KEY={jwt_secret}")
    print()
    print("⚠️  IMPORTANT: Keep these keys secure and never commit them to version control!")