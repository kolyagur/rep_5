#import models

from sqlalchemy import insert,select,or_,and_
from sqlalchemy.sql.selectable import Values

from models import User, Address
from db import engine,Base
            
Base.metadata.create_all(engine)

def insert_one_user():
    stmt = insert(User).values(
        name='Johnny',
        fullname='John Carter'
    )
    with engine.connect() as conn:
        conn.execute(stmt)

#insert_one_user()

def insert_many_users(values):
    stmt = insert(User)
    with engine.connect() as conn:
        conn.execute(stmt,values)

#values = [    
#    {'name': 'Anna', 'fullname': 'Anna Karelina'},
#    {'name': 'Guido', 'fullname': 'Guido Van Rossum'}
#]        

#insert_many_users(values)

#def select_users():
#    stmt = select(User)
#    with engine.connect() as conn:
#        return list(conn.execute(stmt))

#print(select_users())

#for row  in select_users():
#    print(row)

#for row in select_users():
#    print(f'{row.name} has fullname: {row.fullname}')    

def select_users():
    stmt = (
        select(User.name,User.fullname)
    .where(
        #or_(
           # and_(User.id>=2,User.id<=2),
           # User.name.in_(["Peter","Johnny"])
        #)
        (
            User.name.like('%o%')
        )
    ).order_by(User.name.asc())
    )
    with engine.connect() as conn:
        return list(conn.execute(stmt))

for row in select_users():
    print(f'{row.name} has fullname: {row.fullname}') 