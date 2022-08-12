import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), unique=True, nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    password= Column(Integer, unique=False, nullable=False)
    posts = relationship('post', backref='user', lazy=True)
    friends = relationship('friend', backref='user', lazy=True)
    followers = relationship('followers', backref='user', lazy=True)
    my_saved= relationship('saved', backref='user', lazy=True)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(100),unique=False, nullable=False)
    text = Column(String(300),unique=False, nullable=False)
    likes = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    saved_post = relationship('saved', backref='post',lazy=True)

class Friend(Base):
    __tablename__ = 'friends'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    friend_id = Column(Integer, ForeignKey('user.id'))

class Follower(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    follower_id = Column(Integer, ForeignKey('user.id'))

class Saved(Base):
    __tablename__ = 'saved'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e