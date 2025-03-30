import sqlalchemy as db
from sqlalchemy import *
from sqlalchemy_utils import *
import scope_wrapper
import matplotlib.pyplot as plt


#creates a connection and if DB does not exist it creats it
engine = db.create_engine("mysql+pymysql://root:@localhost/rigoldb")#pip install pymysql otherwise this will not work
meta = MetaData()
if not database_exists(engine.url):
    create_database(engine.url)
connection = engine.connect()

#creates table with the folowing "settings", any variable settings (float,int etc needs to be imported form the lib )
test_table=Table("scope",meta,Column("id", Integer, primary_key=True),
                 Column("voltage", Float))
meta.create_all(engine)

Scope=scope_wrapper.Scope("TCPIP0::169.254.226.9::INSTR")
data= Scope.takemeasurement(" CHAN1","NORMal","ASCii")

#inserts data in the database from the measurments
for i in range(len(data)):
    stmt =  insert(test_table).values(voltage = data[i])
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()

plt.plot(data)
plt.show()
