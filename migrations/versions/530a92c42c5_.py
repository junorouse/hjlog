"""empty message

Revision ID: 530a92c42c5
Revises: 3255e6bed08
Create Date: 2016-08-09 19:46:36.752946

"""

# revision identifiers, used by Alembic.
revision = '530a92c42c5'
down_revision = '3255e6bed08'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('photo', 'datetime')
    op.drop_column('photo', 'title')
    op.drop_column('photo', 'description')
    op.add_column('post', sa.Column('private', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'private')
    op.add_column('photo', sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('photo', sa.Column('title', sa.VARCHAR(length=30), autoincrement=False, nullable=True))
    op.add_column('photo', sa.Column('datetime', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    ### end Alembic commands ###
