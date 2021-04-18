import services
import users
import locations
import bookings

# users functions
add_user = users.add_user
update_membership = users.update_membership
update_location = users.update_location
get_user_details = users.get_user_details

#services functions
add_services = services.add_services
get_service_id_from_name = services.get_service_id_from_name
get_service = services.get_service
update_availabilty = services.update_availabilty
select_availabilty = services.select_availabilty
delete_service = services.delete_service
get_servicelist = services.get_servicelist

#locations
add_location = locations.add_location
get_loc_list = locations.get_loc_list
get_loc_id = locations.get_loc_id
get_loc_name = locations.get_loc_name
get_loc_user = locations.get_loc_user

#bookings
create_booking = bookings.create_booking
