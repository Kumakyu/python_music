import sys
from sqlalchemy import Column, String, Date, Integer, Numeric, DateTime
from database import Base
from database import ENGINE

#テーブル：Holidayの定義
class Station(Base):
    __tablename__ = 'stations'
    seq = Column('seq', Integer, primary_key = True) #駅番号
    name = Column('name', String(20)) #駅名
    kilo = Column('kilo',Numeric(6,2)) #東京駅からの距離

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)