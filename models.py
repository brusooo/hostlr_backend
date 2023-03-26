from sqlalchemy import Column, Boolean, String ,BigInteger


from database import Base


class User(Base):
    __tablename__ = "Users"
    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    email = Column(String, nullable=False)
    mobileNumber = Column(BigInteger, nullable=False)
    feePaid = Column(Boolean, nullable=False , default=False)
