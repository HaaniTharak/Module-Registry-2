from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

db = SQLAlchemy()

class Packages_table(db.Model):
    ID = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    NAME = db.Column(db.String(255), unique=True, nullable=True)
    VERSION = db.Column(db.String(50), nullable=True)
    RAMPUP = db.Column(db.Float, nullable=True)
    CORRECTNESS = db.Column(db.Float, nullable=True)
    BUSFACTOR = db.Column(db.Float, nullable=True)
    RESPONSIVEMAINTAINER = db.Column(db.Float, nullable=True)
    LICENSESCORE = db.Column(db.Float, nullable=True)
    GOODPINNINGPRACTICE = db.Column(db.Float, nullable=True)
    PULLREQUEST = db.Column(db.Float, nullable=True)
    NETSCORE = db.Column(db.Float, nullable=True)
    URL = db.Column(db.String(99),nullable = True)


def add_package(Name,Version,ratings,URL):
    new_package = Packages_table(NAME = Name,VERSION = Version,
        NETSCORE = ratings["NetScore"],
        RAMPUP = ratings["RampUp"],
        CORRECTNESS = ratings["Correctness"],
        BUSFACTOR = ratings["BusFactor"],
        RESPONSIVEMAINTAINER = ratings["ResponsiveMaintainer"],
        LICENSESCORE = ratings["License"],
        URL = URL
        )
    db.session.add(new_package)
    db.session.commit()

def query_package(Query):
    Name = Query.Name.Name
    Version = Query.Version.Version
    if Version == None:
        result = db.session.query(Packages_table).filter_by(NAME = Name).all()
    else:
        result = db.session.query(Packages_table).filter_by(NAME = Name,VERSION=Version).all()
    return result

def query_byID(PackageID):
    ID = PackageID.ID
    return db.session.query(Packages_table).filter_by(ID = ID).all()

def query_all_packages():
    return db.session.query(Packages_table).all()

def reset_all_packages():
    db.session.query(Packages_table).delete()
    db.session.commit()

def reset_ID_packages(PackageID):
    ID = PackageID.ID
    db.session.query(Packages_table).filter_by(ID=ID).delete()
    db.session.commit()

def query_ratings(PackageID):
    ID = PackageID.ID
    return db.session.query(Packages_table).filter_by(ID=ID).all()

    


