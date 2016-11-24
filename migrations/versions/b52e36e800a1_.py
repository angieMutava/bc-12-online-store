"""empty message

Revision ID: b52e36e800a1
Revises: 539de34e7663
Create Date: 2016-11-24 01:45:54.158806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b52e36e800a1'
down_revision = '539de34e7663'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'product_image')
    op.drop_column('store', 'store_image')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('store', sa.Column('store_image', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('products', sa.Column('product_image', sa.VARCHAR(), autoincrement=False, nullable=False))
    ### end Alembic commands ###