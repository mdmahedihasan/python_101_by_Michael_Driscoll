from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from test1 import Album, Artist


engine = create_engine("sqlite:///mymusic.db", echo=True)

# create a session
Session = sessionmaker(bind=engine)
session = Session()

res = session.query(Artist).filter(Artist.name=="MXPX").first()

session.delete(res)
session.commit()