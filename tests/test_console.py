#!/usr/bin/python3
""" teste file for console.py """
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """this will test the console"""

    def test_help(self):
        """test if help works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        output = "EOF  all  count  create  destroy  help  quit  show  update"
        self.assertTrue(output in f.getvalue())

    def test_create(self):
        """test if create works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertTrue(type(f.getvalue()) == str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create noclass")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")

    def test_quit(self):
        """test if quit works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertTrue(f.getvalue() == "")


if __name__ == "__main__":
    unittest.main()
