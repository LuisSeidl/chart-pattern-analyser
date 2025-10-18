from sqlalchemy import (Column, BigInteger, String, ForeignKey, Boolean, TIMESTAMP, PrimaryKeyConstraint, Text,
                        ForeignKeyConstraint)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.sqltypes import Numeric


Base = declarative_base()

class EurUsd_Daily(Base):
    __tablename__ = 'eur_usd_daily'
    date = Column(TIMESTAMP, primary_key=True)
    open = Column(Numeric(9,5), nullable=False)
    high = Column(Numeric(9,5), nullable=False)
    low = Column(Numeric(9,5), nullable=False)
    close = Column(Numeric(9,5), nullable=False)
    volume = Column(BigInteger)

    def __init__(self, date, open, high, low, close, volume=0):
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume