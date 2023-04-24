
import pytest
from functions.file_functions import read_from_file, write_to_file

def test_file_io_functions(tmp_path):
    filename = tmp_path / "test.txt"
    s = "hello world\n"
    write_to_file(s, filename)
    assert read_from_file(filename) == s