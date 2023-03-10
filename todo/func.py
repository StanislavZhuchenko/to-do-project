__all__ = ['username_check', 'password_check']
from re import search, match


def username_check(login: str):
    error = None
    starts = r'^[a-zA-Z_]'
    # user doesn't use symbols in login
    notcontain = r'[\W]'
    if len(login) < 3:
        error = 'Minimum length of login 4 symbols'
    elif match(starts, login) is None:
        error = 'Username must be start with alphabet characters'
    elif search(notcontain, login):
        error = 'Username must not be contain any special symbols'

    return error


def password_check(password):
    error = None
    """
    The function to check the validity of password
    :param password: string, length minimum 6, maximum 16 symbols. Required minimum 1 number, 1 letter in lowercase and
    1 letter in uppercase.
    :return: string, if the conditions are true - 'Password is valid', if false - an error about what is going wrong
    """
    patterns_errors = {'[$#@]': 'Password required minimum 1 symbol from $#@',
                       '[\d]': 'Password required minimum 1 number between 0-9',
                       '[a-z]': 'Password required minimum 1 lowercase letter',
                       '[A-Z]': 'Password required minimum 1 uppercase letter'
                       }
    if not 6 <= len(password) <= 16:
        error = 'Minimum length password 6, maximum 16 symbols'
        return error

    for pattern in patterns_errors:
        if search(pattern, password) is None:
            error = patterns_errors[pattern]
        return error


if __name__ == '__main__':
    # print(login_check('Stas'))
    # print(login_check('@1231dsad'))
    # print(login_check('Shiuhfe@jlkj'))
    # print(login_check('dsadajkj213123k'))
    print(password_check('1hdsFaasdqwe1#31'))
    # print(password_check('fsd123#@'))



