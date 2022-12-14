"""empty message

Revision ID: 4e786fd22231
Revises: a62fea7c6e89
Create Date: 2022-06-05 16:03:46.708457

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4e786fd22231'
down_revision = 'a62fea7c6e89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artist', 'genres')
    op.drop_column('venue', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('genres', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    op.add_column('artist', sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
