from logics.database.models import UserType

dict_ui_key_role = {
    'СУПЕРКОРИСТУВАЧ': UserType.ROOT,
    'АДМІНІСТРАТОР': UserType.ADMIN,
    'КОРИСТУВАЧ': UserType.USER
}
