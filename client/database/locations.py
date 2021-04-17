import connect
''' add the actual address now its gonna work more like users can have multiple addresses
    has address and lims to userid
 '''

def add_location(locationsDict):
    """  args {name: string,
               address: string
               city: string,
               user_id: int,
               postcode: string}
        returns location id """
    conn = None
    try:
        conn = connect.db_connection()
        print(conn)
        c = conn.cursor()
        c.execute("INSERT INTO locations(name, address, city, user_id,postcode)\
                    VALUES(%s,%s,%s,%s,%s)\
                    RETURNING location_id;",(locationsDict['name'],locationsDict['address'],
                    locationsDict['city'],locationsDict['user_id'],locationsDict['postcode']))
        conn.commit()
        location_id = c.fetchall()[0]
        c.close()
        conn.close()
        return location_id
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


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
