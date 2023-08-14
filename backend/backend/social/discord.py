import requests
from django.contrib.auth.models import Permission
from social_core.exceptions import AuthException
from social_core.backends.discord import DiscordOAuth2 as BaseDiscordOAuth2


ALLOWED_GUILDS = [
    '673601282946236417'  # Commander Spellbook
]


def is_member_of_guild(backend, details, response, uid, user, *args, **kwargs):
    if backend.name == 'discord':
        api = f'https://{backend.HOSTNAME}/api/users/@me/guilds'
        headers = {
            'Authorization': f'Bearer {response["access_token"]}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        r = requests.get(api, headers=headers)
        if r.status_code == 200:
            guilds = r.json()
            for guild in guilds:
                if guild['id'] in ALLOWED_GUILDS:
                    return
            raise AuthException(backend, 'You must join the Commander Spellbook Discord server to use this site.')
        else:
            raise AuthException(backend, 'Could not reach Discord API.')


def set_default_permissions(user, is_new, *args, **kwargs):
    if user is not None and is_new:
        permissions = Permission.objects.filter(codename__in=['view_variantsuggestion', 'add_variantsuggestion', 'change_variantsuggestion'])
        user.user_permissions.add(*permissions)


class DiscordOAuth2(BaseDiscordOAuth2):
    def get_scope(self):
        return super().get_scope() + ['email', 'guilds']

    def pipeline(self, pipeline, pipeline_index=0, *args, **kwargs):
        injected_pipeline = list(pipeline)
        injected_pipeline.insert(3, 'backend.social.discord.is_member_of_guild')
        injected_pipeline.append('backend.social.discord.set_default_permissions')
        return super().pipeline(tuple(injected_pipeline), pipeline_index, *args, **kwargs)