import os
from app import create_app, db
from commands.seed_command import SeedCommand

env = os.getenv("APP_ENV")
print(f"Active environment: * {env} *")
app = create_app(env)

def seed_db():
    SeedCommand().run()