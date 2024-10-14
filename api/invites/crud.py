from .schemas import InviteSchemaCreatePartial, InviteSchemaCreate
from . import utils


async def create_invite(invite_in: InviteSchemaCreatePartial) -> InviteSchemaCreate:
    invite_value = utils.generate_invite_code()

    return InviteSchemaCreate(
        limit=invite_in.limit,
        type=invite_in.type,
        value=invite_value,
        is_activate=True
    )

