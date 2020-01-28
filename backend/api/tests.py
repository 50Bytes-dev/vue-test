from django.test import TestCase

# Create your tests here.
from backend.api.models import *


def generate_test_posts():
    session = vk.Session(
        access_token="ee0452bf382d80b4e94db2c7e4c1dc3d4babc12c66fbbb1d75f88d4f9d6cb10ce56c0b55aac04bdd058c8")
    api = vk.API(session)
    response = api.execute(
        code="""
        var response = API.wall.get({"owner_id": 359659391, "count": 50});
        return response;
        """,
        v="5.103"
    )
    for post in response['items']:
        if Post.objects.filter(post_id=post['id']).exists():
            post_instance = Post.objects.get(id=post['id'])
        else:
            post_instance = Post()
            post_instance.post_id = post['id']
        post_instance.from_id = post['from_id']
        post_instance.date_post = datetime.fromtimestamp(post['date'])
        post_instance.owner_id = post['owner_id']
        post_instance.text = post['text']
        with transaction.atomic():
            post_instance.save()
        for attachment in post['attachments']:
            if attachment['type'] == 'photo':
                photo = attachment['photo']
                if Photo.objects.filter(photo_id=photo['id']).exists():
                    photo_instance = Photo.objects.get(photo_id=photo['id'])
                else:
                    photo_instance = Photo()
                    photo_instance.photo_id = photo['id']
                photo_instance.sizes = photo['sizes']
                photo_instance.text = photo['text']
                photo_instance.post = post_instance
                with transaction.atomic():
                    photo_instance.save()