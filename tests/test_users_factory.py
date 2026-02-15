from app.factories.users_factory import UsersFactory

def test_should_check_users_loaded_when_using_function():
    factory = UsersFactory()
    users = factory.create_users("data/users.json")
    assert len(users) == 1000

def test_should_check_id_first_user_when_using_function():
    factory = UsersFactory()
    users = factory.create_users("data/users.json")
    assert users[0].id == 1

def test_should_check_login_first_user_when_using_function():
    factory = UsersFactory()
    users = factory.create_users("data/users.json")
    assert users[0].login == "user0001"

def test_should_check_age_first_user_when_using_function():
    factory = UsersFactory()
    users = factory.create_users("data/users.json")
    assert users[0].age == 19
