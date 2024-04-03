from .models import User, UserType
from .database import session


def register(username, password, role: UserType, firstname, lastname):
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        print("Користувач з таким ім'ям вже існує")
        return False
    new_user = User(username=username, password=password, role=role, firstname=firstname, lastname=lastname)
    session.add(new_user)
    session.commit()
    print("Реєстрація успішна")
    return new_user


def login(username, password):
    user = session.query(User).filter_by(username=username).first()
    if user and user.password == password:
        access = user.is_access()
        if access is True:
            return user
        else:
            return access
    else:
        return "Неправильне ім'я користувача або пароль"
