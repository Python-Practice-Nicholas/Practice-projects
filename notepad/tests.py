from unittest import TestCase
import os
from strings.notepad.logic import create_dir, create_new_file


class LogicTestCase(TestCase):

    #def tearDown(self):
        #os.rmdir("/home/user/practice-projects/strings/notepad/files")

    def test_create_directory(self):
        new_dir = create_dir()

        self.assertEqual(f"{os.getcwd()}", new_dir)

        os.rmdir("/home/user/practice-projects/strings/notepad/files")


    def test_create_new_file(self):
        new_dir = create_dir()
        file_path = create_new_file(new_dir)

        self.assertEqual("/home/user/practice-projects/strings/notepad/files/newFile.txt", file_path)


   # def test_save_file(self):
       # pass

    #def test_open_file(self):
        

    #def test_write_to_file(self):
        