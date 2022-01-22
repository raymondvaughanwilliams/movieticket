"""empty message

Revision ID: 8949a8ceb0fa
Revises: a5424af51862
Create Date: 2022-01-20 22:19:43.963505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8949a8ceb0fa'
down_revision = 'a5424af51862'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ref_code', sa.String(length=20), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.drop_column('ref_code')

    # ### end Alembic commands ###