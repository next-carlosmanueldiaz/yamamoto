# -*- coding: utf-8 -*-
"""
Librería de creación y uso de mocks de recursos virtuales de SNS (con boto3)
usando MOTO para Tests Unitarios
"""
import boto3
from config import config
#from moto import mock_sns

"""
SNS con boto3

Para usar esta clase es necesario que se agregue 
el decorador @mock_sns de moto en el test donde se use
"""

class SNSCommons:
    def __init__(self):
         """
        Constructor de la clase
        Crea el recurso
        """
        self.sns = None
        self.create_resource()

    def create_resource(self):
        """
        Crea un recurso S3 con MOTO
        Implementa patrón singleton, para crear sólo un recurso
        :return: None
        """
        try:
            # Crea el recurso si no existe previamente (singleton)
            if self.sns is None:
                # Configura una sesión predeterminada, pasando los parámetros necesarios al constructor de la sesión.
                boto3.setup_default_session(region_name=config.region)
                self.sns = boto3.resource('sns', region_name=config.region)
        except Exception as ex:
            print "[snsCommons][create_resource]" + ex.message

    def get_resource(self):
        """
        Retorna el recurso sns creado
        :return: objeto SNS ServiceResource
        """
        return self.sns

    def create_topic(self, topic_name):
        """
        Crea un topic de SNS
        :param topic_name: nombre del topic a crear
        :return: sns.Topic
        """
        topic = self.sns.create_topic(Name=topic_name)
        return topic

    def list_topics(self):
        """
        Lista los topics de SNS
        :return: list(sns.Topic)
        """
        topics = self.sns.topics.all()
        return topics
