import sys
from sqlalchemy import Column, String, Date, Integer, Numeric, DateTime
from database import Base
from database import ENGINE

#テーブル：transportの定義
class Transport(Base):
    __tablename__ = 'transport'
    date = Column('date', Date, primary_key = True) #利用日
    seq = Column('seq', Integer, primary_key = True) #連番
    departure = Column('daparture', String(20)) #出発地
    arrival = Column('arrival', String(20)) #到着地
    via = Column('via', String(40)) #経由/利用交通機関
    amount = Column('amount',Integer) #金額

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)