#gonna write some basic tests
import api
import datetime

#print(api.add_services({'name':'Ladder','available':True,'location':'1','serviceType':"Hire",'points':10}))

#print(api.get_service_id_from_name("Ladder",'1'))

#print(api.get_service('1'))

#print(api.update_availabilty('1',False))

#print(api.select_availabilty('1'))

#print(api.delete_service('1'))

'''print(api.add_user({'firstname': 'Aqsa',
         'surname': 'Saied',
         'email': 'aqsa.saied@gmail.com',
         'password': 'pass',
         'membership': False,
         'locId':1
         }))'''

#print(api.update_membership(True,1))

#print(api.get_loc_id('Leeds'))
#print(api.get_loc_name(1))
#print(api.get_loc_list())

#print(api.update_location(1,1))
'''print(api.create_booking({
        'startdate':datetime.date(2021,4,17),
        'enddate':datetime.date(2021,4,19),
        'userId':'1',
        'serviceId':'2'
        }))'''

#print(api.get_user_details(1))  

