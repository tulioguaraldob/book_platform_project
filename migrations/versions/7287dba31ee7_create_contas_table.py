"""create contas table

Revision ID: 7287dba31ee7
Revises: e62a7b351c2c
Create Date: 2024-12-30 17:39:04.668840

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7287dba31ee7'
down_revision: Union[str, None] = 'e62a7b351c2c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'contas',
        sa.Column('id', sa.Integer, sa.Identity(), primary_key=True),
        sa.Column('holder', sa.String(255), nullable=False),
        sa.Column('balance', sa.Float, nullable=False),
    )


def downgrade():
    op.drop_table('contas')
