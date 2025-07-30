from sqlalchemy import *
engine=create_engine('sqlite:///C:\\Users\\lenov\\OneDrive\\Desktop\\Beat\\college.db',echo=True)
engine
meta=MetaData()
students=Table('students',meta,Column('id',Integer,primary_key=True),Column('name',String),Column('lastname',String),)
meta.create_all(engine)
departments=Table('departments',meta,Column('dep_id',Integer,primary_key=True),Column('dep_name',String),)
meta.create_all(engine)
marks=Table('marks',meta,Column('mark_id',Integer,primary_key=True),Column('sub1',Float),Column('sub2',Float),Column('sub3',Float),Column('sub4',Float),Column('sub5',Float),)
meta.create_all(engine)

conn=engine.connect()
ins=students.insert().values(name='Ranjinee',lastname='R')
conn.execute(students.insert(),[{'name':'Nahva','lastname':'C'},{'name':'Nadiya','lastname':'Hafsath'},{'name':'Nafeesathul','lastname':'Kamaru'}])
for i in conn.execute(students.select()):
    print(i)
conn.commit()
conn.close()
conn.execute(students.select()).fetchone()
conn.execute(students.select()).fetchmany(3)
result=conn.execute(students.select())
result.fetchall()
conn.execute(students.select().where(students.c.id>2)).fetchall()
conn.execute(select([students]))
t=text('select students.name,students.lastname from students')
conn.execute(t).fetchall()

t=text('select students.name,students.lastname from students where students.name = :x')
conn.execute(t,{'x':'Nahva'}).fetchall()


st=students.alias()
conn.execute(st.select()).fetchall()

conn.execute(students.update().where(students.c.lastname=='C').values(lastname='noor'))
conn.execute(students.select()).fetchall()

conn.execute(students.delete().where(students.c.id==4))
conn.execute(students.select()).fetchall()

add=Table('address',meta,Column('id',Integer,primary_key=True),Column('St_id',Integer,ForeignKey('students.id')),Column('city',String),Column('country',String),)
meta.create_all(engine)

conn.execute(add.insert(), [
 {'St_id':1, 'city':'Mannarkkad', 
'country':'India'},
 {'St_id':1, 'city':'Makkaraparamba', 
'country':'India'},
 {'St_id':3, 'city':'Jubilee Hills Hyderabad', 
'country':'India'},
 {'St_id':4, 'city':'MG Road Bangaluru', 
'country':'India'},
 {'St_id':2, 'city':'Cannought Place new Delhi', 
'country':'India'},
 ])

conn.execute(add.select()).fetchall()



engine=create_engine("mysql://root:root@localhost/college",echo=True)
meta=MetaData()
student=Table(students,meta,Column('id',Integer,primary_key=True),Column('name',VARCHAR(50)),Column('lastname',VARCHAR(50)),)
meta.create_all(engine)
conn=engine.connect()
conn.execute()


