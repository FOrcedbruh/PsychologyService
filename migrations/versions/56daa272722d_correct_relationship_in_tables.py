"""Correct relationship in tables

Revision ID: 56daa272722d
Revises: fc8bb0ae365a
Create Date: 2024-10-14 11:25:39.277995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '56daa272722d'
down_revision: Union[str, None] = 'fc8bb0ae365a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('invites', 'from_user_id')
    op.drop_column('invites', 'to_user_id')
    op.add_column('users', sa.Column('invite_id', sa.Integer(), nullable=False))
    op.drop_constraint('users_get_invite_id_fkey', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'invites', ['invite_id'], ['id'])
    op.drop_column('users', 'get_invite_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('get_invite_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users_get_invite_id_fkey', 'users', 'invites', ['get_invite_id'], ['id'])
    op.drop_column('users', 'invite_id')
    op.add_column('invites', sa.Column('to_user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('invites', sa.Column('from_user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
