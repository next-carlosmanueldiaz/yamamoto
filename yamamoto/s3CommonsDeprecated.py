# -*- coding: utf-8 -*-
"""
Librería de creación y uso de mocks de recursos virtuales de S3 (con boto)
usando MOTO para Tests Unitarios
"""
import boto
from boto.s3.key import Key as Key_Boto_s3
from moto import mock_s3_deprecated

"""
s3 con boto
"""
class s3CommonsDeprecated():
    def __init__(self):
        self.bucket = None
        self.name = None
        self.conn = None
        self.create_conn()

    @mock_s3_deprecated
    def create_conn(self):
        try:
            # conexion a s3 con el método predeterminado en boto.
            if self.conn is None:
                self.conn = boto.connect_s3()
        except Exception as ex:
            print "[s3CommonsDeprecated][create_resource]" + ex.message

    def create_bucket(self, s3d_bucket_name):
        try:
            # crea un  bucket dentro del s3 conecta
            self.bucket = self.conn.create_bucket(s3d_bucket_name)
            self.name = s3d_bucket_name
        except Exception as ex:
            print "[s3CommonsDeprecated][create_bucket]" + ex.message

    def get_bucket(self, s3d_bucket_name):
        try:
            # crea un  bucket dentro del s3 conecta
            self.bucket = self.conn.get_bucket(s3d_bucket_name)
            return self.bucket

        except Exception as ex:
            print "[s3CommonsDeprecated][get_bucket]" + ex.message

    def put(self, s3d_bucket_name, origen, destino):
        try:

            bucketobj = self.conn.get_bucket(s3d_bucket_name)
            k = Key_Boto_s3(bucketobj)
            k.key = destino
            k.set_contents_from_filename(origen)

        except Exception as ex:
            print "[s3CommonsDeprecated][PUT]" + ex.message
