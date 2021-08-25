from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Favourite Places" table
class FavouritePlaces(base):
    __tablename__ = "FavoritePlaces"
    id = Column(Integer, primary_key=True)
    country_name = Column(String)
    capital_city = Column(String)
    population = Column(String)
    language = Column(String)


# create a class-based model for the "Friends" table
class Friends(base):
    __tablename__ = "Friends"
    friendId = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    meet_place = Column(String)
    years_known = Column(Integer, primary_key=False)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# create records for the "Favourite Places" table
finland = FavouritePlaces(
    country_name="Finland",
    capital_city="Helsinki",
    population="5.518 million",
    language="Finnish",
)

france = FavouritePlaces(
    country_name="France",
    capital_city="Paris",
    population="67.06 million",
    language="French",
)

peru = FavouritePlaces(
    country_name="Peru",
    capital_city="Lima",
    population="32.51 million",
    language="Spanish",
)

spain = FavouritePlaces(
    country_name="Spain",
    capital_city="Madrid",
    population="46.94 million",
    language="Spanish",
)

sweden = FavouritePlaces(
    country_name="Sweeden",
    capital_city="Stockholm",
    population="10.23 million",
    language="Swedish",
)

# add and commit records
# session.add(finland)
# session.add(france)
# session.add(peru)
# session.add(spain)
# session.add(sweden)
# session.commit()

# correct country name error in Sweden
# place5 = session.query(FavouritePlaces).filter_by(id=5).first()
# place5.country_name = "Sweden"
# session.commit()

# query "Favourite Places"
# places = session.query(FavouritePlaces)
# for place in places:
#     print(
#         place.id,
#         place.country_name,
#         place.capital_city,
#         place.population,
#         place.language,
#         sep=" | "
#     )


# create records for the "Friends" table
adam_clarke = Friends(
    first_name="Adam",
    last_name="Clarke",
    meet_place="Primary School",
    years_known=32
)

rachel_clark = Friends(
    first_name="Rachel",
    last_name="Clark",
    meet_place="Gilbert Road",
    years_known=35
)

james_hall = Friends(
    first_name="James",
    last_name="Hall",
    meet_place="Gorilla Run",
    years_known=14
)

ian_brannan = Friends(
    first_name="Ian",
    last_name="Brannan",
    meet_place="Greenwich",
    years_known=8
)

claire_mcswiggan = Friends(
    first_name="Claire",
    last_name="McSwiggan",
    meet_place="University",
    years_known=17
)

lisa_vince = Friends(
    first_name="Lisa",
    last_name="Vince",
    meet_place="University",
    years_known=17
)

# add and commit friends
# session.add(adam_clarke)
# session.add(rachel_clark)
# session.add(james_hall)
# session.add(ian_brannan)
# session.add(claire_mcswiggan)
# session.add(lisa_vince)
# session.commit()

# query all friends
my_friends = session.query(Friends)
for friend in my_friends:
    print(
        friend.friendId,
        friend.first_name + " " + friend.last_name,
        friend.meet_place,
        friend.years_known,
        sep=" | "
    )
