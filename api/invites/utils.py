from fastapi import Body
from .schemas import InviteSchemaCreatePartial
import string
import random



INVITE_LENGTH: int = 9


def generate_invite_code(l: int = INVITE_LENGTH) -> str:
    all_symbols = string.ascii_uppercase + string.digits
    result = ''.join(random.choice(all_symbols) for _ in range(l))
    return result



def invite_form(invite_in: InviteSchemaCreatePartial = Body()) -> InviteSchemaCreatePartial:
    return InviteSchemaCreatePartial(
        limit=invite_in.limit,
        type=invite_in.type,
        is_activate=invite_in.is_activate
    )