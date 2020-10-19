import json
import unittest

from app import app


class AppTest(unittest.TestCase):
    def test_document_status(self):
        tester = app.test_client(self)
        response = tester.get('/customers/document-status?document_id=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_document_status_document_id_not_exist(self):
        tester = app.test_client(self)
        response = tester.get('/customers/document-status?document_id=100000')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content_type, 'application/json')

    def test_digitized_document(self):
        tester = app.test_client(self)
        response = tester.get('/customers/digitized-document?document_id=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_fetch_documents(self):
        tester = app.test_client(self)
        response = tester.get('/documents/fetch-documents?document_id=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_update_document(self):
        tester = app.test_client(self)
        data = {
            'document_id': 1,
            'invoice_id': 'new_invoice'
        }
        response = tester.put('/documents/update-document', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_add_field(self):
        tester = app.test_client(self)
        data = {
            'document_id': 1,
            'fields': [
                {
                    'name': 'new_column_2',
                    'type': 'int',
                    'can_be_null': True,
                    'default': '0'
                }
            ]
        }
        response = tester.post('/documents/add-field', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')

    def test_modify_field(self):
        tester = app.test_client(self)
        data = {
            'document_id': 1,
            'fields': [
                {
                    'name': 'p1',
                    'type': 'text',
                    'can_be_null': True,
                    'default': ''
                }
            ]
        }
        response = tester.put('/documents/modify-field', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')


if __name__ == "__main__":
    unittest.main()
