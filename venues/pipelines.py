from django.shortcuts import redirect
from social_core.backends.linkedin import LinkedinOAuth2

__author__ = 'edx'
from social_core.pipeline.partial import partial


def get_avatar(backend, strategy, details, response, user=None, *args, **kwargs):
    url = None
    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
        # if you need a square picture from fb, this line help you
        url = "http://graph.facebook.com/%s/picture?width=150&height=150" % response['id']
    if backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal', '')
    if backend.name == 'google-oauth2':
        url = response['image'].get('url')
        ext = url.split('.')[-1]
    if isinstance(backend, LinkedinOAuth2):
        url = response['pictureUrl']
    if url:
        user.avatar = url
        user.save()