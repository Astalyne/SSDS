import os

import sys
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Status,StatusType, FoodCategory,FoodCategoryHistory,FoodItem,Employee,EmployeeType,Transaction,CustomerOrder

engine = create_engine('sqlite:///ssds.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

statustype1= StatusType(ststid="001",description="AVAILABLE",entity="ABCD")
statustype2= StatusType(ststid="002",description="UNAVAILABLE",entity="CDVD")
statustype3= StatusType(ststid="003",description="WORKING",entity="ASDF")
session.add(statustype1)
session.add(statustype2)
session.add(statustype3)
session.commit()

