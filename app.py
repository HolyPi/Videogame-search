from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
# host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/videogames')
# client = MongoClient(host=f'{host}?retryWrites=false')
# db = client.get_default_database()
client = MongoClient()
db = client.get_default_database('GameView')
videogames = db.videogames
favorites = db.favorites
favorites.delete_many({})


#Videogames database was disabled because it was going to be pushed to Heroku app twice
videogames.delete_many({})
videogames.insert_many(

    [{'title': 'Persona 1', 'price': 50.99, 'image': "https://images-na.ssl-images-amazon.com/images/I/51GYSIjaXAL._SX342_.jpg", 'platform': "http://gotrend.co.za/wp-content/uploads/2015/09/2000px-Playstation_logo.png?w=640"},
    {'title': 'Persona 2', 'price': 52.22, 'image': "https://upload.wikimedia.org/wikipedia/en/thumb/9/93/Persona_2_IS_NA_box_art.png/220px-Persona_2_IS_NA_box_art.png", 'platform': "https://www.feirox.com/rivu/2015/02/PPSSPP-PSP-emulator-1.png"},
    {'title': 'Persona 3', 'price': 22.22, 'image': "https://images-na.ssl-images-amazon.com/images/I/81yTRFRr23L.AC_SL1500_.jpg", 'platform': "https://www.feirox.com/rivu/2015/02/PPSSPP-PSP-emulator-1.png"},
    {'title': 'Persona 4', 'price': 30.99, 'image': "https://m.media-amazon.com/images/S/aplus-media/sota/3eee2f4f-63aa-4c47-b5cd-dc7621d70d1d.jpg", 'platform': "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/PlayStation_logo.svg/1200px-PlayStation_logo.svg.png"},
    {'title': 'Persona 5', 'price': 59.99, 'image': "https://media.gamestop.com/i/gamestop/10146553/Persona-5", 'platform': "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/PlayStation_logo.svg/1200px-PlayStation_logo.svg.png"},
    {'title': 'Ace Attorney Investigations: Miles Edgeworth', 'price': 20.99, 'image': "https://upload.wikimedia.org/wikipedia/en/thumb/0/0d/Ace_Attorney_Investigations_Miles_Edgeworth_Game_Cover.jpg/220px-Ace_Attorney_Investigations_Miles_Edgeworth_Game_Cover.jpg", 'platform': "https://www.ssbwiki.com/images/4/44/DSSymbol.svg"},
    {'title': 'Ace Attorney Investigations 2', 'price': 14.99, 'image': "https://upload.wikimedia.org/wikipedia/en/2/20/GK2boxart.jpg", 'platform': "https://www.ssbwiki.com/images/4/44/DSSymbol.svg"},
    {'title': 'Phoenix Wright: Ace Attorney', 'price': 15.99, 'image': "https://upload.wikimedia.org/wikipedia/en/7/73/Phoenix_Wright_-_Ace_Attorney_Coverart.png", 'platform': "https://www.ssbwiki.com/images/4/44/DSSymbol.svg"},
    {'title': 'Apollo Justice: Ace Attorney', 'price': 40.99, 'image': "https://upload.wikimedia.org/wikipedia/en/0/0b/Apollo-justice-english-cover.jpg", 'platform': "https://www.ssbwiki.com/images/4/44/DSSymbol.svg"},
    {'title': 'Phoenix Wright: Ace Attorney − Dual Destinies', 'price': 30.99, 'image': "https://upload.wikimedia.org/wikipedia/en/b/bd/Ace_Attorney_5_cover.jpg", 'platform': "https://cdn.worldvectorlogo.com/logos/nintendo-3ds.svg"},
    {'title': 'Phoenix Wright: Ace Attorney − Trials and Tribulations', 'price': 15.99, 'image': "https://upload.wikimedia.org/wikipedia/en/5/51/Pw3-cover-english.jpg", 'platform': "https://www.ssbwiki.com/images/4/44/DSSymbol.svg"},
    {'title': 'Metal Gear Solid: Snake Eater', 'price': 14.99, 'image': "https://http2.mlstatic.com/metal-gear-solid-3-snake-eater-ps2-patch-leia-desc-D_NQ_NP_778579-MLB31218428427_062019-F.jpg", 'platform': "http://gotrend.co.za/wp-content/uploads/2015/09/2000px-Playstation_logo.png?w=640"},
    {'title': 'Danganronpa trilogy', 'price': 59.99, 'image': "https://images-na.ssl-images-amazon.com/images/I/81sLio1GoeL._AC_SX430_.jpg", 'platform': "http://gotrend.co.za/wp-content/uploads/2015/09/2000px-Playstation_logo.png?w=640" },
    {'title': 'Metal Gear Solid', 'price': 70.55, 'image': "https://upload.wikimedia.org/wikipedia/en/3/33/Metal_Gear_Solid_cover_art.png", 'platform': "http://gotrend.co.za/wp-content/uploads/2015/09/2000px-Playstation_logo.png?w=640" },
    {'title': 'Metal Gear Solid 2: Sons of Liberty', 'price': 23.44, 'image': "https://upload.wikimedia.org/wikipedia/en/6/6a/Metalgear2boxart.jpg", 'platform': "http://gotrend.co.za/wp-content/uploads/2015/09/2000px-Playstation_logo.png?w=640" },
    {'title': 'Metal Gear Solid 4: Guns of the Patriots', 'price': 21.55, 'image': "https://upload.wikimedia.org/wikipedia/en/4/4b/Mgs4us_cover_small.jpg", 'platform': "http://gotrend.co.za/wp-content/uploads/2015/09/2000px-Playstation_logo.png?w=640" },
    {'title': 'Metal Gear Solid: Peace Walker', 'price': 23.99, 'image': "https://upload.wikimedia.org/wikipedia/en/8/86/Metal_Gear_Solid_Peace_Walker_Cover_Art.jpg", 'platform': "https://www.feirox.com/rivu/2015/02/PPSSPP-PSP-emulator-1.png" },
    {'title': 'Metal Gear Solid V: Ground Zeroes', 'price': 49.99, 'image': "https://upload.wikimedia.org/wikipedia/en/0/07/MGSV_Ground_Zeroes_boxart.jpg", 'platform': "http://gotrend.co.za/wp-content/uploads/2015/09/2000px-Playstation_logo.png?w=640" },
    {'title': 'Metal Gear Solid V: The Phantom Pain', 'price': 59.99, 'image': "https://upload.wikimedia.org/wikipedia/en/8/8f/Metal_Gear_Solid_V_The_Phantom_Pain_cover.png", 'platform': "http://gotrend.co.za/wp-content/uploads/2015/09/2000px-Playstation_logo.png?w=640" },
    {'title': 'Night In The Woods', 'price': 19.99, 'image': "https://s2.gaming-cdn.com/images/products/3448/orig/night-in-the-woods-switch-cover.jpg", 'platform': "https://vignette.wikia.nocookie.net/fantendo/images/5/50/NintendoSwitchLogoBlack.png/revision/latest?cb=20180518004200" },
    {'title': 'Hollow Knight', 'price': 19.99, 'image': "https://media.gamestop.com/i/gamestop/10174149/Hollow-Knight", 'platform': "https://vignette.wikia.nocookie.net/fantendo/images/5/50/NintendoSwitchLogoBlack.png/revision/latest?cb=20180518004200" },
    {'title': 'Phoenix Wright: Ace Attorney − Justice for All', 'price': 14.99, 'image': "https://vignette.wikia.nocookie.net/aceattorney/images/d/db/JFA_Box_Art.png/revision/latest?cb=20151028223624", 'platform': "https://www.ssbwiki.com/images/4/44/DSSymbol.svg"},
    {'title': 'Professor Layton vs. Phoenix Wright: Ace Attorney', 'price': 59.99, 'image': "https://upload.wikimedia.org/wikipedia/en/d/d0/Laytonvsaceattorneycover.jpg", 'platform': "https://cdn.worldvectorlogo.com/logos/nintendo-3ds.svg"},
    {'title': 'The World Ends With You', 'price': 27.99, 'image': "https://media.gamestop.com/i/gamestop/10157970/The-World-Ends-with-You-Final-Remix", 'platform': "https://vignette.wikia.nocookie.net/fantendo/images/5/50/NintendoSwitchLogoBlack.png/revision/latest?cb=20180518004200"},
    {'title': 'Yakuza 0', 'price': 14.49, 'image': "https://images-na.ssl-images-amazon.com/images/I/810MJ9frzIL._SL1500_.jpg", 'platform': "http://gotrend.co.za/wp-content/uploads/2015/09/2000px-Playstation_logo.png?w=640"},
    {'title': 'Fire Emblem Fates Birthright', 'price': 19.99, 'image': "https://media.gamestop.com/i/gamestop/10126804/Fire-Emblem-Fates-Birthright?$pdp$", 'platform': "https://cdn.worldvectorlogo.com/logos/nintendo-3ds.svg"} ])

# @app.route('/login')
# def login():
#     "Prompts user to log-in"

# Route for handling the login page logic
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     "Login for user"
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect(url_for('home'))
#     return render_template('login.html', error=error)

@app.route('/profile')
def profile():
    "Shows user profile, and favorites"
    
@app.route('/quiz')


@app.route('/')
def game_index():
    """Show all videogames."""
    return render_template('game_index.html', videogames=videogames.find())

    # f = db.videogames.findone()
    # # q = request.args.get("search")
    # querystring = {"search": f}


@app.route('/videogame/<videogame_id>', methods=['GET'])
def game_show(videogame_id):
    "Individual Videogame"
    videogame = videogames.find_one({'_id': ObjectId(videogame_id)})
    return render_template('game_show.html', videogame=videogame)




@app.route("/videogame/<videogame_id>/favorited", methods=['GET'])
def add_to_favorites(videogame_id):
    "Adds to the favorites"
    game = videogames.find_one({'_id': ObjectId(videogame_id)})
    print(game)
    favoritesGame = {
        'title': game.get('title'),
        'price': game.get('price'),
        'image': game.get('image'),
        'platform': game.get('platform')
     }
    favorites.insert_one(favoritesGame)
    return redirect(url_for('game_index', game=game))

@app.route('/search')
def search_game(videogame_id):
    "Search for games"

    f = request.args.get("search")
    querystring = {"search": f}

    return render_template('game_show.html', querystring=querystring)

@app.route("/favorites")
def view_favorite():
    "Views favorites"
    total = 0
    Nothing = ""
    for videogame in favorites.find():
        total += int(videogame['price'])
    if favorites.count_documents({}) <= 0:
        Nothing = "Add some games to your favorites!"
    return render_template("favorite.html", favorites=favorites.find(), total = total, Nothing = Nothing)


@app.route("/favorites/<videogame_id>/delete", methods=['POST'])
def remove_from_favorite(videogame_id):
    "Removes from favorites"
    favorites.delete_one({'_id':ObjectId(videogame_id)})
    return redirect(url_for('view_favorite'))
