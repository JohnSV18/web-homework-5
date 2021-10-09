from flask import Flask, request, redirect, render_template, url_for
from flask_pymongo import PyMongo, MongoClient
from bson.objectid import ObjectId
import os

############################################################
# SETUP
############################################################

app = Flask(__name__)
host = os.environ.get("MONGO_URI", 'mongodb+srv://Johnze:Pokemon100@plantsdb.vsybz.mongodb.net/myFirstDatabase') + '?retryWrites=true&w=majority'
app.config["MONGO_URI"] = host
mongo = PyMongo(app)

############################################################
# ROUTES
############################################################

@app.route('/')
def plants_list():
    """Display the plants list page."""

    plants_data = mongo.db.plants.find({})

    context = {
        'plants': plants_data,
    }
    return render_template('plants_list.html', **context)

@app.route('/about')
def about():
    """Display the about page."""
    return render_template('about.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    """Display the plant creation page & process data from the creation form."""
    plant = request.form.get('plant_name')
    variety =  request.form.get('variety'),
    photo_url = request.form.get('photo'),
    date_planted = request.form.get('date_planted') 
    
    if request.method == 'POST':
        
        new_plant = {
            'name': plant,
            'variety': variety,
            'photo_url': photo_url,
            'date_planted':date_planted 
        }
     
        result = mongo.db.plants.insert_one(new_plant)
        result_id = result.inserted_id
       

        return redirect(url_for('detail', plant_id=result_id))

    else:
        return render_template('create.html')

@app.route('/plant/<plant_id>')
def detail(plant_id):
    """Display the plant detail page & process data from the harvest form."""

   
    plant_to_show = mongo.db.plants.find_one({
        '_id': ObjectId(plant_id)
    })

    
    harvests = list(mongo.db.harvest.find({
        'plant_id':plant_id
    }))

    context = {
        'plant' : plant_to_show,
        'harvest': harvests,
        'plant_id' : ObjectId(plant_id)
    }

    return render_template('detail.html', **context)

@app.route('/harvest/<plant_id>', methods=['POST'])
def harvest(plant_id):
    """
    Accepts a POST request with data for 1 harvest and inserts into database.
    """
    date_harvested = request.form.get("date_harvested")
    harvested_amount = request.form.get("harvested_amount")
    input_string = harvested_amount
    
    new_harvest = {
        'quantity': input_string,
        'date': date_harvested,
        'plant_id': ObjectId(plant_id)
    }

    
    mongo.db.harvest.insert_one(new_harvest)

    return redirect(url_for('detail', plant_id=plant_id))

@app.route('/edit/<plant_id>', methods=['GET', 'POST'])
def edit(plant_id):
    """Shows the edit page and accepts a POST request with edited data."""
    if request.method == 'POST':

        plant = {
            'name': request.form.get('plant_name'),
            'variety': request.form.get('variety'),
            'photo_url': request.form.get('photo'),
            'date_planted': request.form.get('date_planted')

        }

        mongo.db.plants.update_one( {'_id': ObjectId(plant_id)}, {'$set': plant})


        
        return redirect(url_for('detail', plant_id=plant_id))
    else:
       
        plant_to_show = mongo.db.plants.find_one({'_id': ObjectId(plant_id)})

        context = {

            'plant': plant_to_show['name'],
            'variety': plant_to_show['variety'],
            'photo_url' : plant_to_show['photo_url'],
            'date_planted': plant_to_show['date_planted']
        }

        return render_template('edit.html', **context)

@app.route('/delete/<plant_id>', methods=['POST'])
def delete(plant_id):
   
    mongo.db.plants.delete_one({'_id': ObjectId(plant_id)})

    mongo.db.harvest.delete_many({'plant_id':plant_id})

    return redirect(url_for('plants_list'))
    

if __name__ == '__main__':
    app.run(debug=True) 

