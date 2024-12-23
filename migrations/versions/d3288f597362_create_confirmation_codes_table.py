"""create confirmation codes table

Revision ID: d3288f597362
Revises: f31484e38c7b
Create Date: 2024-12-16 13:39:09.440076

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd3288f597362'
down_revision: Union[str, None] = 'f31484e38c7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('confirmation_codes',
    sa.Column('value', sa.String(), nullable=False),
    sa.Column('user_email', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('users', 'interests',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'interests',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=False)
    op.drop_table('confirmation_codes')
    # ### end Alembic commands ###
