import random

from .models import Content, Gender

def find_content(gender):
    content = Content.query.filter(Content.gender == Gender[gender]).all()
    return random.choice(content)
