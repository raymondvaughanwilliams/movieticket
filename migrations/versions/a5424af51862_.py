"""empty message

Revision ID: a5424af51862
Revises: 801a21755379
Create Date: 2022-01-19 19:32:54.549741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5424af51862'
down_revision = '801a21755379'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.alter_column('refund_requested',
               existing_type=sa.BOOLEAN(),
               nullable=True)
        batch_op.alter_column('refund_granted',
               existing_type=sa.BOOLEAN(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.alter_column('refund_granted',
               existing_type=sa.BOOLEAN(),
               nullable=False)
        batch_op.alter_column('refund_requested',
               existing_type=sa.BOOLEAN(),
               nullable=False)

    # ### end Alembic commands ###
