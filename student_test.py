import unittest
from unittest.mock import patch
import io
import sys

from student import calculate_grade, main


# -------- Grade calculation tests --------

def test_grade_S():
    assert calculate_grade(95) == "S"


def test_grade_A():
    assert calculate_grade(85) == "A"


def test_grade_B():
    assert calculate_grade(70) == "B"


def test_grade_C():
    assert calculate_grade(55) == "C"


def test_grade_D():
    assert calculate_grade(45) == "D"


def test_grade_F():
    assert calculate_grade(30) == "F"


# -------- Main output test --------

def test_main_output(capsys):
    main()

    captured = capsys.readouterr()
    output = captured.out

    assert "--- Grade Criteria ---" in output
    assert "--- Student Details ---" in output
    assert "Name: neha" in output
    assert "Department: BCA" in output
    assert "Semester: 3" in output
    assert "--- Subject Marks ---" in output
    assert "Average Marks: 90.0" in output
    assert "Final Grade: S" in output