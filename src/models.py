from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# #Usando modelo con tabla de relaciones:
# association_table = db.Table('association', db.Model.metadata,
#     db.Column('Users', db.String, db.ForeignKey('users.id'), primary_key=True),
#     db.Column('Movies', db.String, db.ForeignKey('movies.id'), primary_key=True),
#     db.Column('Planets', db.String, db.ForeignKey('planets.id'), primary_key=True),
#     db.Column('Character', db.String, db.ForeignKey('characters.id'), primary_key=True),
# )

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    usersname = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    subscription_date = db.Column(db.Date)
    is_login = db.Column(db.Boolean)
    # planets = db.relationship('Planets', secondary=association_table, backref='Users')
    # movies = db.relationship('Movies', secondary=association_table, backref='Users')
    # characters = db.relationship('Characters', secondary=association_table, backref='Users')

    def __repr__(self):
        return '<Users %r>' % self.usersname

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Profiles(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(20))
    firstname = db.Column(db.String(20))
    nickname = db.Column(db.String(6))
    imgurl = db.Column(db.String())
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True) #Define un user a un perfil únicamente
    users = db.relationship(Users)


class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    gravity = db.Column(db.Integer)        
    population = db.Column(db.Integer)
    climate = db.Column(db.String)
    terrain = db.Column(db.String)
    surface_water = db.Column(db.Integer)
    url = db.Column(db.String, nullable=False) 
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    users = db.relationship(Users) 
        
 
class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable=False)
    year  = db.Column(db.Integer, nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    users = db.relationship(Users)


class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String)
    skin_color = db.Column(db.String)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    users = db.relationship(Users)


#Creamos las tablas de favoritos. Opción1:
class FavoriteCharacters(db.Model):
    __tablename__ = "favorite_characters"
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    users = db.relationship(Users) 
    characters = db.relationship (Characters)

class FavoritePlanets(db.Model):
    __tablename__ = "favorite_planets"
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    users = db.relationship(Users) 
    planets = db.relationship (Planets)
