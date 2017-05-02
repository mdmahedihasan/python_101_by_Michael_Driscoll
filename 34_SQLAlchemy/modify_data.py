from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from test1 import Album, Artist

engine = create_engine("sqlite:///mymusic.db", echo=True)

# create a session
Session = sessionmaker(bind=engine)
session = Session()

# querying for a record in the artist table
res = session.query(Artist).filter(Artist.name == "New").first()
print(res.name)

# changing the name
res.name = "New Name"
session.commit()

# editing album data
artist, album = session.query(Artist, Album).filter(Artist.id == Album.artist_id).filter(
    Album.title == "Hell is for wimps").first()

album.title = "Step up to the microphone"
session.commit()
