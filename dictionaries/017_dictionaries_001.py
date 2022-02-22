import pytest

def make_user(key_, value_):
    dict1 = dict()
    dict1.update({'name': key_})
    dict1.update({'age': value_})
    return dict1


def format_user(some_dict):
    string1 = str()
    string1 = f"{some_dict.get('name')}, {str(some_dict.get('age'))}"
    return string1


@pytest.mark.parametrize(
    ('name', 'age', 'result'),
    [
        ('Phil', 30, 'Phil, 30'),
    ]
)
def test_format_user(name, age, result):
    assert format_user(make_user(name, age)) == result


if __name__ == "__main__":
    print(format_user(make_user('Joe', 25)))