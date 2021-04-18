import connect
import services

def create_booking(bDict):
    """
    Create a new booking for a user to rent/borrow a service
    """
    sql = "INSERT INTO Bookings (start_date, end_date, user_id, service_id)\
           VALUES (%s, %s, %s, %s) RETURNING booking_id;"

    booking_id = None
    conn = None

    try:
        conn = connect.db_connection()
        c = conn.cursor()
        c.execute(sql, (bDict['startdate'], bDict['enddate'], bDict['userId'], bDict['serviceId'],))
        booking_id = c.fetchone()[0]
        services.update_availabilty(bDict['serviceId'],False)
        conn.commit()
        c.close()
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return booking_id
