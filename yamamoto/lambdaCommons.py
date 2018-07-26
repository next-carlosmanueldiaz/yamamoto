# -*- coding: utf-8 -*-
"""
Librería de creación y uso de mocks de recursos virtuales de Lambdas
usando MOTO para Tests Unitarios
"""
import boto3
import filesCommons

class lambdaCommons():
    """
    Constructor de la clase
    Crea un cliente
    """
    def __init__(self):
        self.lambda_name = None
        self.lambda_function = None
        self.create_client()

    """
    Crea el recurso de una lambda
    """
    def create_client(self):
        try:
            self.lambda_function = boto3.client('lambda')
        except Exception as ex:
            print "[lambdaCommons][create_resource]" + ex.message

    """
    Crea una lambda
    """
    def create_lambda(self, lambda_name):
        try:
            self.lambda_name = lambda_name
            self.lambda_function.create_function(
                FunctionName = self.lambda_name,
                Runtime='python2.7',
                Role='test-iam-role',
                Handler='lambda_function.lambda_handler',
                Code={'ZipFile': filesCommons.get_test_zip_file1()},
                Description='test lambda function',
                Timeout=3,
                MemorySize=128,
                Publish=True,
            )
        except Exception as ex:
            print "[lambdaCommons][create_lambda]" + ex.message