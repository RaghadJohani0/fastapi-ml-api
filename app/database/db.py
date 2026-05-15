from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///resume.db"

engine = create_engine(
    DATABASE_URL
)
