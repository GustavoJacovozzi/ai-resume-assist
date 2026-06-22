from app.database import engine, Base
from app.models.resume import Resume
Base.metadata.create_all(bind= engine)

