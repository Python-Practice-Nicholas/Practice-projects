from unittest import TestCase
import os
from notepad.logic import create_dir, create_new_file


class LogicTestCase(TestCase):

    def tearDown(self):
        os.rmdir("/home/user/practice-projects/strings/notepad/files")

   # @classmethod
    #def tearDownClass(cls):
        #os.remove("home/user/notepad/files/newFile.txt")
       # os.rmdir("home/user/notepad/files")
    
    def test_create_directory(self):
        new_dir = create_dir()

        self.assertEqual(f"{os.getcwd()}", new_dir)

        # os.rmdir("home/user/practice-projects/notepad/files")


    def test_create_new_file(self):
        #os.rmdir("home/user/practice-projects/notepad/files")
        #new_dir = create_dir()
        file_path = create_new_file(os.getcwd())

        self.assertEqual("/home/user/practice-projects/notepad/files/newFile.txt", file_path)


   # def test_save_file(self):
       # pass

    #def test_open_file(self):
        

    #def test_write_to_file(self):
        