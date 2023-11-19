"""empty message

Revision ID: 8ccf39e2118d
Revises: 57e46a98dac5
Create Date: 2023-11-19 19:21:07.586438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ccf39e2118d'
down_revision = '57e46a98dac5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('module',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('view_name', sa.String(length=128), nullable=True),
    sa.Column('package_name', sa.String(length=128), nullable=True),
    sa.Column('version', sa.String(length=128), nullable=True),
    sa.Column('hash', sa.String(length=256), nullable=True),
    sa.Column('id_file', sa.String(length=36), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('module')
    # ### end Alembic commands ###
