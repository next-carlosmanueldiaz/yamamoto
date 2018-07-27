# YamaMoto
Tests Unitarios con Moto

Una de las formas de crear tests unitarios es mediante el uso de la librería [Moto](https://github.com/spulec/moto), 
que crea Mocks de servicios AWS. Para estandarizar este proceso y no reinventar contínuamente la rueda, hemos creado este grupo de clases, que integran servicios de Amazon con Moto, con lo que además conseguimos que el código de los tests sea más reducido y legible.


## Install

pip install -r requirements.txt

## Tests Unitarios con Moto
Una de las maneras de realizar tests unitarios es crear previamente un entorno "virtual" que 
simule en local los servicios de AWS. Moto realiza esta tarea por nosotros, realizando mocks de 
los servicios AWS, con lo que no se realizan peticiones a ningún servicio externo.

Para crear tests unitarios, por tanto, la idea es crear en el test primero el entorno de AWS 
que necesitemos, tal y como se crean de forma real, pero usando el decorador de Moto como 
envoltorio (por ejemplo, @mock_s3) en las funciones en las que se use boto3. 
De esta manera, las acciones todas las peticiones realizadas con boto3 serán automáticamente 
mockeadas.

Este es un ejemplo de uso, para testear una lambda que necesita previamente 
un bucket con un fichero dentro dentro:

```python
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
```





