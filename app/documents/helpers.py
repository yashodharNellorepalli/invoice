ALLOWED_EXTENSIONS = ["pdf"]


def get_field_query(field):
    name = field.get('name')
    type_ = field.get('type')

    if field.get('can_be_null'):
        null_ = ''
    else:
        null_ = 'NOT NULL'

    default = field.get('default')

    if default is not None:
        default = f"DEFAULT '{default}'"

    return " ".join(map(str, list(filter(lambda x: x, [name, type_, null_, default]))))


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
