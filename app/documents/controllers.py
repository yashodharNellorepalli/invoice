from flask import Blueprint, jsonify, request
from .services import get_documents_info, update_document, add_fields_to_document, modify_fields_to_document
from app.utils.constants import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST


documents_module = Blueprint('documents', __name__, url_prefix='/documents')


@documents_module.route('/fetch-documents', methods=['GET'])
def fetch_documents():
    request_args = request.args
    status, documents_info = get_documents_info(request_args)

    if not status:
        response_data = {
            "error": documents_info
        }

        return jsonify(response_data), HTTP_400_BAD_REQUEST

    response_data = {
        "documents": documents_info
    }

    return jsonify(response_data), HTTP_200_OK


@documents_module.route('/update-document', methods=['PUT'])
def update_document_internal():
    request_args = request.get_json()
    document_id = request_args.get('document_id')

    if not document_id:
        response_data = {
            "error": "document_id does not exist"
        }

        return jsonify(response_data), HTTP_400_BAD_REQUEST

    status, x = update_document(request_args)

    if not status:
        response_data = {
            "error": x
        }

        return jsonify(response_data), HTTP_400_BAD_REQUEST

    response_data = {
        "status": 'Success'
    }

    return jsonify(response_data), HTTP_200_OK


@documents_module.route('/add-field', methods=['POST'])
def add_new_field():
    request_args = request.get_json()
    document_id = request_args.get('document_id')
    fields = request_args.get('fields')

    if not document_id:
        response_data = {
            "error": "document_id does not exist"
        }

        return jsonify(response_data), HTTP_400_BAD_REQUEST

    if not fields:
        response_data = {
            "error": "fields does not exist"
        }

        return jsonify(response_data), HTTP_400_BAD_REQUEST

    status, x = add_fields_to_document(fields)

    if not status:
        response_data = {
            "error": x
        }

        return jsonify(response_data), HTTP_400_BAD_REQUEST

    response_data = {
        "status": 'Success'
    }

    return jsonify(response_data), HTTP_201_CREATED


@documents_module.route('/modify-field', methods=['PUT'])
def modify_existing_fields():
    request_args = request.get_json()
    document_id = request_args.get('document_id')
    fields = request_args.get('fields')

    if not document_id:
        response_data = {
            "error": "document_id does not exist"
        }

        return jsonify(response_data), HTTP_400_BAD_REQUEST

    if not fields:
        response_data = {
            "error": "fields does not exist"
        }

        return jsonify(response_data), HTTP_400_BAD_REQUEST

    status, x = modify_fields_to_document(fields)

    if not status:
        response_data = {
            "error": x
        }

        return jsonify(response_data), HTTP_400_BAD_REQUEST

    response_data = {
        "status": 'Success'
    }

    return jsonify(response_data), HTTP_200_OK
