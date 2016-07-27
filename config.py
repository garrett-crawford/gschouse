import os 
basedir = os.path.abspath(os.path.dirname(__file__))

# path of the database file (required by Flask-SQLAlchemy)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

# where we will store SQLALchemy-migrate data files
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# suppresses the warning when running stuff
SQLALCHEMY_TRACK_MODIFICATIONS = False