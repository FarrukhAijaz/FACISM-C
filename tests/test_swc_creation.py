# tests/test_swc_creation.py
import unittest
from swc.swc_creator import create_new_swc

class TestSWCCreation(unittest.TestCase):
    def test_swc_creation(self):
        swc_name = "TestSWC"
        directory = "/tmp"
        create_new_swc(swc_name, directory)
        # Add assertions to check the created files