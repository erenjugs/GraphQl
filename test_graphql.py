# test_graphql.py
"""
Tests for GraphQl module.
"""

import unittest
from graphql import GraphQl

class TestGraphQl(unittest.TestCase):
    """Test cases for GraphQl class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GraphQl()
        self.assertIsInstance(instance, GraphQl)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GraphQl()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
