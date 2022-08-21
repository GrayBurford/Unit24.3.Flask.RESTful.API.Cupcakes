"""Flask app for Cupcakes"""

from models import db, connect_db, Cupcake
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///cupcakes'

# Set this to false or SQLAlchemy will yell at you
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Print all SQL statements to the terminal (helpful for debugging)
app.config['SQLALCHEMY_ECHO']  = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "ABC123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route('/', methods=["GET"])
def home_page():
    """Render homepage or base.html"""

    return render_template('base.html')


@app.route('/api/cupcakes', methods=["GET"])
def get_all_cupcakes():
    """Render JSON info about all cupcakes in DB"""

    all_cupcakes = Cupcake.query.all()
    serialized_cupcakes = [cc.serialize() for cc in all_cupcakes]
    print(serialized_cupcakes)

    return jsonify(cupcakes=serialized_cupcakes)


@app.route('/api/cupcakes/<int:cc_id>', methods=["GET"])
def get_one_cupcake(cc_id):
    """Render JSON info about one cupcake by id"""

    cc = Cupcake.query.get_or_404(cc_id)
    return jsonify(cupcake=cc.serialize())


@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Create instance of one cupcake"""

    new_cc = Cupcake(
        flavor=request.json['flavor'], 
        size=request.json['size'], 
        rating=request.json['rating'], 
        image=request.json['image']
    )

    db.session.add(new_cc)
    db.session.commit()
    json_response = jsonify(cupcake=new_cc.serialize())
    return (json_response, 201)


@app.route('/api/cupcakes/<int:cc_id>', methods=["PATCH"])
def update_one_cupcake(cc_id):
    """Edit info for one cupcake from id passed through URL"""

    cupcake = Cupcake.query.get_or_404(cc_id)

    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()
    json_resp = jsonify(cupcake.serialize()), 200
    return json_resp
    

@app.route('/api/cupcakes/<int:cc_id>', methods=["DELETE"])
def delete_one_cupcake(cc_id):
    """Deletes a cupcake from DB based on ID passed through URL"""

    cupcake = Cupcake.query.get_or_404(cc_id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify({"message" : "deleted that cupcake"})


# TEST THESE ROUTES THROUGH INSOMNIA OR POSTMAN
# POSTMAN