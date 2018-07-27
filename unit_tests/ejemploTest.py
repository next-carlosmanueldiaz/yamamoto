# -*- coding: utf-8 -*-
import const
import unittest
from yamamoto.s3Commons import s3Commons
from yamamoto.dynCommons import dynCommons

from moto import mock_s3, mock_dynamodb2

from lambdas.lambdaFile import *

class ejemploTestCase(unittest.TestCase):
    def setUp(self):

        pass

    """
    Test unitario de la lambda
    """

    @mock_s3
    @mock_dynamodb2
    def test_lambda_handler(self):
        """
        Test unitario de la lambda
        :return: None
        """

        # S3
        # -------------------------------------------------------------------------------------------------------------
        bucket_name = 'bucketname'
        myS3 = s3Commons() # Instanciamos la librería, que crea el recurso s3
        myS3.create_bucket(bucket_name) # creamos el bucket info
        myS3.put(bucket_name, 'recursos/info.txt', 'info/info.txt') # subimos el fichero al bucket

        # DYNAMODB
        # -------------------------------------------------------------------------------------------------------------
        myDyn = dynCommons() # Instanciamos la librería, que crea el recurso dynamoDB
        myDyn.create_table(const.table_config_name, const.table_config_schema, const.table_config_attributes)
        myDyn.put_item(const.config_miscelanea_reg) # Insertamos registo
        results = myDyn.table_query('keyName', 'MISCELANEA') # Consultamos la tabla
        assert 'keyName' in results['Items'][0]
        assert results['Items'][0]['keyName'] == 'MISCELANEA'

        # Ejecución de la lambda
        evento = {}
        result = lambda_handler(evento, "")
        self.assertEqual(result, True)









