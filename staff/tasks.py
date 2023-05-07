"""Contains tasks to be executed for methods."""

from sqlalchemy import select
import httpx

from ...settings import Settings
from .schemas import Permission
from .models import UserInfo


async def send_notification(permission: Permission):
    department = permission.user_group.split("/")[2]
    designation = permission.user_group.split("/")[3]
    # fetcch hod user id
    # select user_id from user_group_membership inner join keycloak_group on user_group_membership.group_id = keycloak_group.id where keycloak_group.name='Heads' and keycloak_group.parent_group in (select id from keycloak_group where keycloak_group.name='CSE')

    user_id = select([text('user_id')]).select_from(user_group_membership.join(keycloak_group, user_group_membership.c.group_id == keycloak_group.c.id)).where(and_(keycloak_group.c.name == text('Heads'), keycloak_group.c.parent_group))
    stmt = select(UserInfo).where(UserInfo.user_id == user_id)
    token = db.execute(stmt)
    notification = {
        "to": token,
        "date": {
            "title": "original title", "message": "original message"
        }
    }
    fcmAPI = "https://fcm.googleapis.com/fcm/send"

    # use request
    response = httpx.post(
        fcmAPI,
        notification
    )

    print(f"department = {department}, designation={designation}")
