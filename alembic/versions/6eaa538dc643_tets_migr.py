"""tets migr

Revision ID: 6eaa538dc643
Revises: 
Create Date: 2023-06-07 17:31:33.287794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6eaa538dc643'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shop_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_code', sa.String(length=20), nullable=True),
    sa.Column('category_name', sa.String(length=100), nullable=True),
    sa.Column('subcategory_code', sa.String(length=20), nullable=True),
    sa.Column('subcategory_name', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('photo', sa.String(length=250), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('size', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('full_name', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('reg_date', sa.TIMESTAMP(), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('phone', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('shop_items')
    # ### end Alembic commands ###