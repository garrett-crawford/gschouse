from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
player = Table('player', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=32)),
    Column('main', String(length=32)),
    Column('ranking', Integer),
    Column('description', String(length=512)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['player'].columns['description'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['player'].columns['description'].drop()
