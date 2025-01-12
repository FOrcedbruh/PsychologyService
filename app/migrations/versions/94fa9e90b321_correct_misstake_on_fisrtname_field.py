"""correct misstake on fisrtname field

Revision ID: 94fa9e90b321
Revises: 2d930527aa9f
Create Date: 2025-01-12 14:34:50.278186

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '94fa9e90b321'
down_revision: Union[str, None] = '2d930527aa9f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('firstname', sa.String(), nullable=False))
    op.drop_column('users', 'fisrtname')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('fisrtname', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('users', 'firstname')
    # ### end Alembic commands ###
