import connect

def get_loc_list():
    """
    Returns entire list of location names
    """
    sql = "SELECT name FROM Locations;"
    conn = None
    locations = None

    try:
        conn = connect.db_connection()
        c = conn.cursor()
        c.execute(sql, ())
        locations = c.fetchall()
        c.close()
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
    return locations

def get_loc_name(locId):
    """
    Returns locations name for a single id
    """
    sql = "SELECT name FROM Locations WHERE location_id=%s;"
    conn = None
    location = None

    try:
        conn = connect.db_connection()
        c = conn.cursor()
        c.execute(sql, (locId,))
        location = c.fetchone()[0]
        c.close()
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
    return location

def get_loc_id(name):
    """
    Returns locations id for a location name
    """
    sql = "SELECT location_id FROM Locations WHERE name=%s;"
    conn = None
    locId = None

    try:
        conn = connect.db_connection()
        c = conn.cursor()
        c.execute(sql, (name,))
        locId = c.fetchone()[0]
        c.close()
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
    return locId
