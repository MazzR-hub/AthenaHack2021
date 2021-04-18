from flask import Blueprint, render_template, request
import sys
sys.path.append("./database")
import api

listings = Blueprint('listings', __name__, template_folder='templates', static_folder='static')


@listings.route('/listings', methods=['GET', 'POST'])
def display_listings():
    listedItems = api.get_servicelist()
    if listedItems is None:
        listedItems = ['No listings available in your area! Why don\'t you add one?']
    '''listenItems is an array of tuples will this work in this format or does it need
        to be converted to a 2 dimentional array'''
    return render_template('listings.html', listedItems=listedItems)

@listings.route('/create-listing',methods=['GET','POST'])
def create_listing():
    if request.method == "POST":
        data = request.data
        print(data) 
        #add code to get the information from the form
        '''service_id = api.add_services({'name':'placeholder',
                          'available':'placeholder',
                          'location':'placeholder',
                          'serviceType':'placeholder',
                          'points':'placeholder',
                          'price':'placeholder',
                          'user_id':'placeholder'})
        if service_id == None:
            # add a fail statement. "throw an error or like send to a page "'''

    else:
        #get address list from user_id
        #how are we getting the user_id
        locationItems = api.get_loc_user(1)
        #acting as a placeholder till we know the exact details
        #return render_template('htmlfilename.html',locationItems=locationItems)
