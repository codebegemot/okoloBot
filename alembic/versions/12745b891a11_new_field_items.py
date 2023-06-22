"""new field items

Revision ID: 12745b891a11
Revises: ea4e2ddd3b85
Create Date: 2023-06-15 18:10:08.941393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12745b891a11'
down_revision = 'ea4e2ddd3b85'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shop_items', sa.Column('message_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shop_items', 'message_id')
    # ### end Alembic commands ###