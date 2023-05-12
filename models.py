from sqlalchemy import Column, Boolean, String ,BigInteger
from sqlalchemy import Column, Text
from sqlalchemy.dialects.postgresql import UUID

from database import Base, engine


from database import Base


class User(Base):
    __tablename__ = "Users"
    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    email = Column(String, nullable=False)
    mobileNumber = Column(BigInteger, nullable=False)
    feePaid = Column(Boolean, nullable=False , default=False)
"""Contains ORM models for dlapp - staff"""



class UserInfo(Base):
    """Mapping of `userinfo` table"""

    __tablename__ = "userinfo"

    user_id = Column(UUID(as_uuid=True), primary_key=True)
    token = Column(Text)


Base.metadata.create_all(engine)
