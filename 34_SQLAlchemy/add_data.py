import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from test1 import Album, Artist


engine = create_engine("sqlite:///mymusic.db", echo=True)

# create a session
Session = sessionmaker(bind=engine)
session = Session()

# create an artist
new_artist = Artist(name="NewsBoys")
new_artist.albums = [Album(title="Read all about it",
                           release_date=datetime.date(1988, 12, 1),
                           publisher="Refuge",
                           media_type="CD")]

# add more albums
more_albums = [Album(title="Hell is for wimps",
                     release_date = datetime.date(1990, 7, 15),
                     publisher="Star Song",
                     media_type="CD")]

new_artist.albums.extend(more_albums)

# add the record to the session object
session.add(new_artist)

# commit the record to the database
session.commit()

# add several artists
session.add_all([
    Artist(name="MXPX"),
    Artist(name="Kutless"),
    Artist(name="New")
])
session.commit()