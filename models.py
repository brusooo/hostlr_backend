from sqlalchemy import Column, Boolean, Date, String ,BigInteger, Time

from datetime import date,time
from database import Base



class permission(Base):
    __tablename__ = "permission"
    id = Column(BigInteger, primary_key=True)
    stuid_ = Column(BigInteger)
    from_ = Column(Date, nullable=False)
    to_ = Column(Date, nullable=False)
    accepted_by = Column(String, nullable=False)
    reason_ = Column(String, nullable=False)
    informed_parent_on = Column(Time, nullable=False)
    # feepaid = Column(Boolean, nullable=False , default=False)

    load_instance = True
# class SubmittedData(Base):
#     tablename = 'form_data'

#     id = Column(BigInteger, primary_key=True)
#     name = Column(String,nullable=False)
#     from_ = Column(date,nullable=False)
#     to = Column(date,nullable=False)
#     reason = Column(String,nullable=False)
#     informed_Parennt_On = Column(date,nullable=False)