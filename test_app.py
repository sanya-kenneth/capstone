import os
import unittest
import json
from models import db
from app import create_app


class CapstoneTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app('Testing')
        db.create_all(app=self.app)
        self.client = self.app.test_client()
        self.teacher_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1qRXlRVUpDUVRsQ09UQkVNVEZDTWtWR01VWXdPVGRETlVVMk5UQTRRMFZGTlVNMVJqQkROdyJ9.eyJpc3MiOiJodHRwczovL2Rldi16NTdxMGcyYS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDkwMzcyMjc2Mzg5NTg3MTMzMTEiLCJhdWQiOlsiaHR0cDovLzAuMC4wLjA6ODA4MC8iLCJodHRwczovL2Rldi16NTdxMGcyYS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTc5NzA1Mzk4LCJleHAiOjE1Nzk3OTE3OTgsImF6cCI6IjJnNzc3b2txSlg0QVRucjZvclNKc2NQdmpyU2RPRlpJIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImFkZDpxdWVzdGlvbiIsImRlbGV0ZTpxdWVzdGlvbiIsImVkaXQ6cXVlc3Rpb24iLCJyZWFkOmFuc3dlciIsInJlYWQ6YW5zd2VycyIsInJlYWQ6cXVlc3Rpb24iLCJyZWFkOnF1ZXN0aW9ucyJdfQ.X_FoY2b5H7sQWGUtEqOhcKxOwggjpHEwLE8gCiIvKWcLRvEKweJEjgK-OXMxyNwSOojBBc25BZ5vcx_CEzUR1supkJL-rrkIWV-uaEkIYIc5IErPytROAzsMrivasaY--lxoCetyOqUebIgpZHhFAnP5d_vQNJ6YInT-G8jggWY_1x2wjw2s1cwZwVaqnTcs0VJir_OqqZxvDPCdzrCgd4kuQhTou31-Vdg_UbnuyeqRX2c90tGZ1RuTyrW9hUvU464pAuHnoPSJFnupIUdub0WmullOoVUhYuVZZ-oM2yCUmF2CdiOAX-c0BV2eFIqnGMX09SvyYvvEn8LS5OvDmw'
        self.question = {
                'question': 'What is python?',
                'teacher_id': '12'
            }
        self.header =  {"Authorization":"Bearer {}".format(self.teacher_token)}


    def tearDown(self):
        db.drop_all(app=self.app)
        
    
    def test_api_can_add_question_as_teacher(self):
        response = self.client.post('/questions', json=self.question,
                                    headers=self.header)
        self.assertEqual(response.status_code, 201)
        
    
    def test_api_returns_error_if_a_teacher_tries_to_add_a_question_that_exists(self):
        self.client.post('/questions', json=self.question, headers=self.header)
        response = self.client.post('/questions', json=self.question, headers=self.header)
        response = json.loads(response.data)
        self.assertEqual(response["error"], "Question What is python?already exists")


    def test_api_can_get_questions(self):
        self.client.post('/questions', json=self.question, headers=self.header)
        response = self.client.get('/questions', headers=self.header)
        data = json.loads(response.data)
        self.assertTrue(data["success"])
        self.assertEqual(data["data"][0]["question"], "What is python?")


    def test_api_returns_404_not_found_if_there_no_questions(self):
        response = self.client.get('/questions', headers=self.header)
        response = json.loads(response.data)
        self.assertEqual(response["error"], "There no questions at the moment")
    
    def test_api_gets_one_question(self):
        self.client.post('/questions', json=self.question, headers=self.header)
        response = self.client.get('/questions/1', headers=self.header)
        data = json.loads(response.data)
        self.assertTrue(data["success"])
        self.assertEqual(data["data"]["question"], "What is python?")


    def test_api_returns_404_not_found_if_a_user_tries_to_get_a_question_that_doesnt_exist(self):
        response = self.client.get('/questions/24', headers=self.header)
        response = json.loads(response.data)
        self.assertEqual(response["error"], "Question not found")


    def test_api_can_delete_question_as_teacher(self):
        self.client.post('/questions', json=self.question, headers=self.header)
        r = self.client.delete('/questions/1', headers=self.header)
        data = json.loads(r.data)
        self.assertTrue(data["success"])
        self.assertEqual(data["message"], "Question has been deleted successfuly")

    
    def test_api_returns_404_not_found_error_if_user_tries_to_delete_a_question_that_doesnt_exist(self):
        response = self.client.delete('/questions/3', headers=self.header)
        response = json.loads(response.data)
        self.assertEqual(response["error"], "Question not found")    


    def test_returns_a_403_unauthorised_error_if_teacher_tries_to_add_an_answer(self):
        r = self.client.post('/question/1/answers', headers=self.header)
        data = json.loads(r.data)
        print(data)
        self.assertEqual(data["error"], "Permission not found.")


    def test_api_can_edit_a_question_as_teacher(self):
        new_data = {
                'question': 'What is Java?',
                'teacher_id': '12'
            }
        self.client.post('/questions', json=self.question, headers=self.header)
        r = self.client.patch('/questions/1', json=new_data, headers=self.header)
        res = json.loads(r.data)
        self.assertEqual(res["message"], "update successful")
