"""rename address

Revision ID: db54ce63c9bf
Revises: ae4b75776780
Create Date: 2025-06-15 14:48:08.176576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db54ce63c9bf'
down_revision = 'ae4b75776780'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('departments', 'address', new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    op.alter_column('departments', 'location', new_column_name='address')
    # ### end Alembic commands ###
