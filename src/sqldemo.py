import sqlalchemy as db
from sqlalchemy import *
from sqlalchemy_utils import *
import scoop_wrapper
import matplotlib.pyplot as plt


#creates a connection and if DB does not exist it creats it
engine = db.create_engine("mysql+pymysql://root:@localhost/rigoldb")#pip install pymysql
meta = MetaData()
if not database_exists(engine.url):
    create_database(engine.url)
connection = engine.connect()

#creates table with the folowing "settings", any variable settings (float,int etc needs to be imported form the lib )
test_table=Table("scope",meta,Column("id", Integer, primary_key=True),
Column("sample", Integer),
Column("voltage", Float))
meta.create_all(engine)

scoop=scoop_wrapper.scoop("TCPIP0::169.254.226.9::INSTR")#connects to the scope over lan using these values
data= scoop.takemeasurement("CHAN1","NORMal","ASCii")

plt.plot(data)
plt.show()
