from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from test1 import Album, Artist


engine = create_engine("sqlite:///mymusic.db", echo=True)

# create a session
Session = sessionmaker(bind=engine)
session = Session()

# SELECT
res = session.query(Artist).all()
for album in res:
    print(album.title)

# JOIN
qry = session.query(Artist, Album)
qry = qry.filter(Artist.id==Album.artist_id)
artist, album = qry.filter(Album.title=="Step up to the microphone").first()

# LIKE
res = session.query(Album).filter(Album.publisher.like("S%a%")).all()
for item in res:
    print(item.publisher)