import databases
import ormar
import sqlalchemy

from .config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class PillIntake(ormar.Model):
    class Meta(BaseMeta):
        tablename = "pill_intake"

    id: int = ormar.Integer(primary_key=True)
    intake_date: str = ormar.String(max_length=16, unique=True, nullable=False)
    intake: bool = ormar.Boolean(default=True, nullable=False)


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)
