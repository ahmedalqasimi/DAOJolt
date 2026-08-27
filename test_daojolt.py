# test_daojolt.py
"""
Tests for DAOJolt module.
"""

import unittest
from daojolt import DAOJolt

class TestDAOJolt(unittest.TestCase):
    """Test cases for DAOJolt class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DAOJolt()
        self.assertIsInstance(instance, DAOJolt)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DAOJolt()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
