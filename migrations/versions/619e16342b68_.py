"""empty message

Revision ID: 619e16342b68
Revises: 5ab27106a06f
Create Date: 2022-02-19 17:13:44.368561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '619e16342b68'
down_revision = '5ab27106a06f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('coupons', schema=None) as batch_op:
        batch_op.alter_column('code',
               existing_type=sa.VARCHAR(length=15),
               nullable=True)
        batch_op.alter_column('amount',
               existing_type=sa.FLOAT(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('coupons', schema=None) as batch_op:
        batch_op.alter_column('amount',
               existing_type=sa.FLOAT(),
               nullable=False)
        batch_op.alter_column('code',
               existing_type=sa.VARCHAR(length=15),
               nullable=False)

    # ### end Alembic commands ###