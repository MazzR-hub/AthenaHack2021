import connect

def add_services(servicesDict):
    """
    Add a new service to user table 

    Args:
        userDict: A dictionary in the form
        {'name': [string],
         'available': [boolean],
         'location': [string],
         'serviceType': [string],
         'points': [int],
         }

    Returns:
        service_id if successful

    """
    
    conn = None
    try:
        conn = connect.db_connection()
        print(conn)
        c = conn.cursor()
        c.execute("INSERT INTO services(name, available, type, points,location_id)\
                    VALUES(%s,%s,%s,%s,%s)\
                    RETURNING service_id;",(servicesDict['name'],servicesDict['available'],\
                    servicesDict['serviceType'],servicesDict['points'],servicesDict['location']))
        conn.commit()
        service_id = c.fetchall()[0]
        c.close()
        conn.close()
        return service_id
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def get_service_id_from_name(name,location):
    """ FINISH"""
    details= None
    conn = None
    try:
        conn = connect.db_connection()
        c = conn.cursor()
        c.execute("SELECT service_id FROM services WHERE name =%s AND location_id = %s;",(name,location))

        conn.commit()
        details = c.fetchall()[0]
        c.close()
        conn.close()
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return details


def get_service(service_id):
    """ Gets the information about a service
        sends it back as an array [name,available,location,type,points]"""
    details= None
    conn =None
    try:
        conn = connect.db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM services WHERE service_id =%s;",(service_id))

        conn.commit()
        details = c.fetchall()
        c.close()
        conn.close()
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return details


def update_availabilty(service_id,available):
    """Updates the services availbility

    returns 1 if true
    """
    conn = None
    try:
        conn = connect.db_connection()
        c = conn.cursor()
        c.execute("UPDATE services SET available =%s WHERE service_id =%s;",(available,service_id))
        conn.commit()
        c.close()
        conn.close()
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return 1

def select_availabilty(service_id):
    """ gets the availability of the product
        returns available [boolean] """
    details= None
    conn =None
    try:
        conn = connect.db_connection()
        c = conn.cursor()
        c.execute("SELECT available FROM services WHERE service_id =%s;",(service_id))
        conn.commit()
        details = c.fetchall()[0]
        c.close()
        conn.close()
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return details

def delete_service(service_id):
    """ Delete a service from the system
    args: service_id int
    returns 0 if successful
    1 if failed"""
    conn = None
    try:
        conn = connect.db_connection()
        c = conn.cursor()
        c.execute("DELETE FROM services WHERE service_id =%s;",(service_id))
        conn.commit()
        c.close()
        conn.close()
    except Exception as error:
        print(error)
        return 0
    finally:
        if conn is not None:
            conn.close()
    return 1

