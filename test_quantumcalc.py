# test_quantumcalc.py
"""
Tests for QuantumCalc module.
"""

import unittest
from quantumcalc import QuantumCalc

class TestQuantumCalc(unittest.TestCase):
    """Test cases for QuantumCalc class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QuantumCalc()
        self.assertIsInstance(instance, QuantumCalc)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QuantumCalc()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
