"""empty message

Revision ID: 12c34dff5be5
Revises: 35683577a5dc
Create Date: 2022-06-06 11:21:00.338802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12c34dff5be5'
down_revision = '35683577a5dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shows', 'start_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('start_time', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
