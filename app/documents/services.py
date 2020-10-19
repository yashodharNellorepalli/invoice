from app import mysql
from app.utils.query import select_query, execute_query
from .helpers import get_field_query


def add_document(customer_id, document_status_id=1):
    query = f"INSERT INTO documents (`customer_id`, `document_status_id`) VALUES ('{customer_id}', {document_status_id})"

    return execute_query(query)


def get_document_info(document_id):
    query = f"SELECT * FROM documents WHERE document_id={document_id}"
    status, data = select_query(query)

    if not status:
        return None

    try:
        return data[0]
    except Exception:
        return None


def get_documents_info(filter_params):
    query = f"SELECT * FROM documents WHERE "
    filter_list = [key + " = " + value for key, value in filter_params.items()]
    query += " and ".join(filter_list)
    return select_query(query)


def get_all_document_statuses():
    query = f"SELECT * FROM document_statuses"
    status, data = select_query(query)

    return data


def get_document_status(document_status_id):
    all_document_statuses = get_all_document_statuses()

    if not all_document_statuses:
        return None

    document_status = list(filter(lambda x: str(x.get('document_status_id')) == str(document_status_id), all_document_statuses))

    try:
        return document_status[0]
    except Exception:
        return None


def update_document(params):
    document_id = params.get('document_id')
    set_params = [f" {key}='{value}'" for key, value in params.items() if key != 'document_id']
    set_params = ",".join(set_params)
    query = f"UPDATE documents SET " + set_params + f"WHERE document_id='{document_id}'"

    return execute_query(query)


def add_fields_to_document(fields):
    query = "ALTER TABLE documents " + ",".join([f"ADD COLUMN {get_field_query(field)}" for field in fields])

    return execute_query(query)


def modify_fields_to_document(fields):
    query = "ALTER TABLE documents " + ",".join([f"MODIFY COLUMN {get_field_query(field)}" for field in fields])

    return execute_query(query)

