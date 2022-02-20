"""empty message

Revision ID: 2fe7cc71c5af
Revises: 9ea722e66638
Create Date: 2022-02-19 17:10:07.006871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fe7cc71c5af'
down_revision = '9ea722e66638'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('coupons', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cid', sa.Integer(), nullable=False))
        batch_op.drop_column('id')

    with op.batch_alter_table('orderitems', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'coupons', ['coupon'], ['cid'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orderitems', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'coupons', ['coupon'], ['id'])

    with op.batch_alter_table('coupons', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), nullable=False))
        batch_op.drop_column('cid')

    # ### end Alembic commands ###
