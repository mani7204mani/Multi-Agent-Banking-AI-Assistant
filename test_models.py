from src.database.db import Base, engine
import src.database.models

Base.metadata.create_all(bind=engine)

print("All tables created successfully!")