"""empty message

Revision ID: 93a1567c087f
Revises: 
Create Date: 2022-06-05 14:26:22.906322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93a1567c087f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('genres', sa.String(length=120), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('website_link', sa.String(length=120), nullable=True),
    sa.Column('seeking_venue', sa.String(), nullable=False),
    sa.Column('seeking_description', sa.String(length=120), nullable=True),
    sa.Column('upcoming_shows', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('past_shows', sa.Integer(), nullable=True),
    sa.Column('past_shows_count', sa.Integer(), nullable=True),
    sa.Column('upcoming_shows_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('genres', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('website_link', sa.String(length=120), nullable=True),
    sa.Column('seeking_talent', sa.String(), nullable=False),
    sa.Column('seeking_description', sa.String(length=120), nullable=True),
    sa.Column('Created_at', sa.String(), nullable=True),
    sa.Column('past_shows', sa.Integer(), nullable=True),
    sa.Column('upcoming_shows', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('past_shows_count', sa.Integer(), nullable=True),
    sa.Column('upcoming_shows_count', sa.Integer(), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venue')
    op.drop_table('artist')
    # ### end Alembic commands ###
