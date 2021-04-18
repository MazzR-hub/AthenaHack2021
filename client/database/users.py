from client.database import connect
from passlib.hash import bcrypt

'''table has'''

def add_user(userDict):
    """
    Add a new user to user table

    Args:
        userDict: A dictionary in the form
        {'firstname': [string],
         'surname': [string],
         'email': [string],
         'password': [string],
         'membership': [boolean],
         'locId':[int]
         }

    Returns:
        user_id
    """

    sql = "INSERT INTO Users(first_name, surname, email, password, membership, location_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING user_id;"
    user_id = None
    conn = None

    try:
        conn = connect.db_connection()
        c = conn.cursor()
        c.execute(sql, (userDict['firstname'], userDict['surname'], userDict['email'], bcrypt.hash(userDict['password']), userDict['membership'], userDict['locId'],))
        user_id = c.fetchone()[0]
        conn.commit()
        c.close()
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return user_id

def update_membership(memberBool, userId):
    """
    Update the membership status for a single user

    Args:
        memberBool: the membership status true/false
        userId: the user ID to update
    Returns:
        0 - failure (no rows updated)
        1 - success (row updated)
    """

    sql = "UPDATE Users SET membership = %s WHERE user_id = %s;"
    conn = None
    updatedRows = 0

    try:
        conn = connect.db_connection()
        c = conn.cursor()
        c.execute(sql, (memberBool, userId,))
        updatedRows = c.rowcount
        conn.commit()
        c.close()
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updatedRows

def update_location(locId, userId):
    """
    Update the location for a single user

    Args:
        userId: the user ID to update
        locId: the location ID
    Returns:
        0 - failure (no rows updated)
        1 - success (row updated)
    """

    sql = "UPDATE Users SET location_id = %s WHERE user_id = %s;"
    conn = None
    updatedRows = 0

    try:
        conn = connect.db_connection()
        c = conn.cursor()
        c.execute(sql, (locId, userId,))
        updatedRows = c.rowcount
        conn.commit()
        c.close()
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updatedRows

def get_user_details(userId):
    """
    Gets all details for a single user

    Args:
        userId: the user id to get info for
    Returns:
        details: array of [firstname, surname, email, location]
    """

    sql = "SELECT Users.first_name, Users.surname, Users.email, Locations.location_id FROM Users\
        INNER JOIN Locations ON Locations.location_id = Users.location_id\
        WHERE user_id = %s;"
    conn = None
    details = None

    try:
        conn = connect.db_connection()
        c = conn.cursor()
        c.execute(sql, (userId,))
        details = c.fetchall()
        c.close()
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return details

def get_user_details_by_email(email):
    """
    Gets all details for a single user

    Args:
        email: the users email address
    Returns:
        details: array of [userId, firstname, surname, location]
    """

    sql = "SELECT Users.userId, Users.first_name, Users.surname, Locations.location_id FROM Users\
        INNER JOIN Locations ON Locations.location_id = Users.location_id\
        WHERE Users.email = %s;"
    conn = None
    details = None

    try:
        conn = connect.db_connection()
        c = conn.cursor()
        c.execute(sql, (email,))
        details = c.fetchall()
        c.close()
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return details
