"""rename department to departments

Revision ID: ae4b75776780
Revises: 016c70440b9f
Create Date: 2025-06-15 14:41:41.168725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae4b75776780'
down_revision = '016c70440b9f'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###