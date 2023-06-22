"""new migration

Revision ID: aee473ace2f1
Revises: 6eaa538dc643
Create Date: 2023-06-07 17:50:04.230158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aee473ace2f1'
down_revision = '6eaa538dc643'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shop_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shop_media',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_id', sa.String(length=255), nullable=True),
    sa.Column('filename', sa.String(length=255), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['shop_items.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('shop_items', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'shop_items', 'shop_categories', ['category_id'], ['id'])
    op.drop_column('shop_items', 'subcategory_name')
    op.drop_column('shop_items', 'category_code')
    op.drop_column('shop_items', 'category_name')
    op.drop_column('shop_items', 'subcategory_code')
    op.drop_column('shop_items', 'photo')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shop_items', sa.Column('photo', sa.VARCHAR(length=250), autoincrement=False, nullable=True))
    op.add_column('shop_items', sa.Column('subcategory_code', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.add_column('shop_items', sa.Column('category_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.add_column('shop_items', sa.Column('category_code', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.add_column('shop_items', sa.Column('subcategory_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'shop_items', type_='foreignkey')
    op.drop_column('shop_items', 'category_id')
    op.drop_table('shop_media')
    op.drop_table('shop_categories')
    # ### end Alembic commands ###