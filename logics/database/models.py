from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserType:
    ROOT = "root"
    ADMIN = "admin"
    USER = "user"


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    role = Column(String)
    access = Column(Integer, default=0)

    def __init__(self, username, password, firstname, lastname, role: UserType):

        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.role = role
        if self.is_root() or self.is_user():
            self.access = 1

    def is_root(self):
        return self.role == UserType.ROOT

    def is_admin(self):
        return self.role == UserType.ADMIN

    def is_access(self):
        if self.access == 0:
            return "Вас не підтверджено!"
        if self.access == 1:
            return True
        if self.access == 2:
            return "Вам заборонили доступ!"

    def is_user(self):
        return self.role == UserType.USER