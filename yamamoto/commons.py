# -*- coding: utf-8 -*-
import sys

"""
Compara un texto que se pasa por parámetro con la salida estandar
"""
def compare_output(self, text):
    if not hasattr(sys.stdout, "getvalue"):
        self.fail("need to run in buffered mode")
    output = sys.stdout.getvalue().strip()  # stdout es una instancia StringIO
    if text in output:
        return True
    else:
        return False