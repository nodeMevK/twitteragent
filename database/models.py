from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Float, ForeignKey, BIGINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ShortMemory(Base):
    __tablename__ = "short_term_memory"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    name = Column(String, index=True)
    tweet_id = Column(BIGINT)
    post = Column(String, index=True)
    timestamp = Column(DateTime(timezone=True))

class LongMemory(Base):
    __tablename__ = "long_term_memory"

    id = Column(Integer, primary_key=True)
    username = Column(String, index=True)
    name = Column(String, index=True)
    tweet_id = Column(Integer)
    post = Column(String, index=True)
    timestamp = Column(DateTime(timezone=True))


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    user_id = Column(Integer)


class Tweets(Base):
    __tablename__ = "tweets_from_user_scrape"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    tweet = Column(String)
    tweet_id = Column(Integer)
    time_stamp = Column(DateTime(timezone=True))
    view_count = Column(Integer)

    #likes = relationship("Like", back_populates=)



class TimeLineTweets(Base):
    __tablename__ = "time_line_tweets"
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    tweet = Column(String)
    tweet_id = Column(Integer)
    time_stamp = Column(DateTime(timezone=True))

'''
class Like(Base):
    __tablename__ = "likes"


class Comment(Base):
    __tablename__ = "comments"'''
  