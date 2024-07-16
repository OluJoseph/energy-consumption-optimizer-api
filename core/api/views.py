from . import api


@api.get('/')
def index():
    return 'hello world'
