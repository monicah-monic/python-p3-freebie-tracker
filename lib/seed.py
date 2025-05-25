#!/usr/bin/env python3
from models import Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebies.db')

freebie1 = Freebie(item_name = 'T-shirt', value =20, company_id= 1, dev_id=3)
freebie2 = Freebie(item_name = 'Mug', value =4, company_id= 3, dev_id=2)
freebie3 = Freebie(item_name = 'Umbrella', value =30, company_id= 8, dev_id=1)
freebie4 = Freebie(item_name = 'Hoodie', value =50, company_id= 2, dev_id=7)

Session = sessionmaker(bind=engine)  
session = Session()  
session.add_all([freebie1, freebie2, freebie3, freebie4])
session.commit()