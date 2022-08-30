"""empty message

Revision ID: 98ae16d9d3c6
Revises: ebe03d11a110
Create Date: 2022-06-05 15:58:20.015628

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '98ae16d9d3c6'
down_revision = 'ebe03d11a110'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artist', 'upcoming_shows_count')
    op.drop_column('artist', 'past_shows')
    op.drop_column('artist', 'upcoming_shows')
    op.drop_column('artist', 'past_shows_count')
    op.drop_constraint('venue_artist_id_fkey', 'venue', type_='foreignkey')
    op.drop_column('venue', 'Created_at')
    op.drop_column('venue', 'past_shows_count')
    op.drop_column('venue', 'past_shows')
    op.drop_column('venue', 'upcoming_shows_count')
    op.drop_column('venue', 'artist_id')
    op.drop_column('venue', 'upcoming_shows')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('upcoming_shows', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    op.add_column('venue', sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('venue', sa.Column('upcoming_shows_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('venue', sa.Column('past_shows', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('venue', sa.Column('past_shows_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('venue', sa.Column('Created_at', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_foreign_key('venue_artist_id_fkey', 'venue', 'artist', ['artist_id'], ['id'])
    op.add_column('artist', sa.Column('past_shows_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('artist', sa.Column('upcoming_shows', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    op.add_column('artist', sa.Column('past_shows', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('artist', sa.Column('upcoming_shows_count', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
