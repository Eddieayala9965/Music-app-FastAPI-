from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base



from db import engine

Base = declarative_base()


class Artist(Base):
    __tablename__ = 'artist'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Song(Base):
    __tablename__ = 'song'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Playlist(Base):
    __tablename__ = 'playlist'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    artist_id = Column(ForeignKey("artist.id"))
    song_id = Column(ForeignKey("song.id"))

# class Token(Base):
#     access_token: str
#     token_type: str

# class User(Base):
#     username: str


Base.metadata.create_all(engine)

