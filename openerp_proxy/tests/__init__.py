import unittest
from openerp_proxy.utils import AttrDict


class BaseTestCase(unittest.TestCase):
    """Instanciates an ``odoorpc.ODOO`` object, nothing more."""
    def setUp(self):
        import os
        try:
            port = int(os.environ.get('ODOO_TEST_PORT', 8069))
        except ValueError:
            raise ValueError("The port must be an integer")
        self.env = AttrDict({
            'protocol': os.environ.get('ODOO_TEST_PROTOCOL', 'xml-rpc'),
            'host': os.environ.get('ODOO_TEST_HOST', 'localhost'),
            'port': port,
            'dbname': os.environ.get('ODOO_TEST_DB', 'openerp_proxy_test_db'),
            'user': os.environ.get('ODOO_TEST_USER', 'admin'),
            'password': os.environ.get('ODOO_TEST_PASSWORD', 'admin'),
            'super_password': os.environ.get('ODOO_TEST_SUPER_PASSWORD', 'admin'),
        })
