"""ticket and orders tables

Revision ID: 5363bebc5bbb
Revises: 61f978c700a2
Create Date: 2022-01-15 20:50:55.223821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5363bebc5bbb'
down_revision = '61f978c700a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coupons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=15), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'code')
    )
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tickets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('discount_price', sa.Float(), nullable=True),
    sa.Column('genre', sa.String(length=255), nullable=True),
    sa.Column('pub_date', sa.DateTime(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.Column('userr_id', sa.Integer(), nullable=False),
    sa.Column('image_1', sa.String(length=150), nullable=False),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.ForeignKeyConstraint(['userr_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticket', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('time', sa.String(length=255), nullable=True),
    sa.Column('coupon', sa.Integer(), nullable=True),
    sa.Column('refund_requested', sa.Boolean(), nullable=False),
    sa.Column('refund_reason', sa.Text(), nullable=True),
    sa.Column('refund_granted', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['coupon'], ['coupons.id'], ),
    sa.ForeignKeyConstraint(['ticket'], ['tickets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_items')
    op.drop_table('tickets')
    op.drop_table('genres')
    op.drop_table('coupons')
    # ### end Alembic commands ###
