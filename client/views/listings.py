from flask import Blueprint, render_template
from client.database import api

listings = Blueprint('listings', __name__, template_folder='templates', static_folder='static')


@listings.route('/listings', methods=['GET', 'POST'])
def display_listings():
    listedItems = api.get_servicelist()
    if listedItems is None:
        listedItems = ['No listings available in your area! Why don\'t you add one?']
        return ''
    string = ''
    for item in listedItems:
        string += '<li class="list-group-item">'+str(item[0])+str(item[1])+str(item[2])+str(item[3])+str(item[4])+str(item[5])+str(item[6])+str(item[7])+'</li>\n'
    return render_template('listings.html', listedItems=string)

@listings.route('/newlist', methods=['GET', 'POST'])
def display_newlist():
    return render_template('newlist.html')
