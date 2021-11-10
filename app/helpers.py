import uuid


def convert_to_slug(title):
    # title separated by dash, and id ex: this-is-title-1628349812219
    # slug operations
    # replace space on title with dash
    # add uuidv1 and generate the hex version
    return str(title.replace(' ', '-') + '-' + str(uuid.uuid4().int))
