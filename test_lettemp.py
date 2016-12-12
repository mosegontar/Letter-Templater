import os
import shutil
import unittest

from make_new_letter import LetterTemplate

class TestLetTemp(unittest.TestCase):

    def setUp(self):
        self.f = open('lettemp_test.txt', 'w')
        self.cwd = os.getcwd()

    def tearDown(self):
        os.remove(self.f.name)

    def write_contents(self, content):

        self.f.write(content)
        self.f.close()

    def get_template_object(self):
        template = LetterTemplate()
        template.get_template_text()
        return template        

    def test_locate_template(self):
        template = LetterTemplate()
        self.assertTrue(len(template.template_files) > 0)

    def test_read_contents(self):
        self.write_contents('Some testing text :)')
        template = self.get_template_object()

        self.assertEqual(template.content, 'Some testing text :)')

    def test_identify_placeholders(self):
        _content = """Dear {{ NAME }} I work at {{ INSTITUTION }}"""
        self.write_contents(_content)

        template = self.get_template_object()

        self.assertEqual(len(template.placeholders), 2)

    def test_replace_placeholders(self):
        _content = "Dear {{ NAME }} I work at {{ INSTITUTION }}"
        self.write_contents(_content)
        template = self.get_template_object()

        template.replace_placeholders(NAME='Alex', INSTITUTION='Hogwarts')

        self.assertEqual(template.new_letter, "Dear Alex I work at Hogwarts")

    def test_write_letter_to_directory(self):
        _content = "Dear {{ NAME }} I work at {{ INSTITUTION }}"
        self.write_contents(_content)
        template = self.get_template_object()
        
        template.replace_placeholders(NAME='Alex', INSTITUTION='Hogwarts')
        template.save_new_letter('new_file_test.txt', new_directory=False)

        _newf_contents = ''
        with open('new_file_test.txt', 'r') as newf:
            _newf_contents = newf.read()
            newf.close()
            os.remove('new_file_test.txt')

        self.assertEqual(_newf_contents, "Dear Alex I work at Hogwarts")

    def test_new_directory_exists(self):

        _content = "Dear {{ NAME }} I work at {{ INSTITUTION }}"
        self.write_contents(_content)
        template = self.get_template_object()
        
        template.replace_placeholders(NAME='Alex', INSTITUTION='Hogwarts')
        template.save_new_letter('new_file_test.txt')

        dir_contents = os.listdir(self.cwd)
        shutil.rmtree(self.cwd+'/'+'Hogwarts')

        self.assertIn('Hogwarts', dir_contents)

    def test_new_letter_in_new_directory(self):
        _content = "Dear {{ NAME }} I work at {{ INSTITUTION }}"
        self.write_contents(_content)
        template = self.get_template_object()
        
        template.replace_placeholders(NAME='Alex', INSTITUTION='Hogwarts')
        template.save_new_letter('new_file_test.txt')

        new_path = self.cwd+'/'+'Hogwarts'
        dir_contents = os.listdir(new_path)
        shutil.rmtree(new_path)

        self.assertIn('new_file_test.txt', dir_contents)




if __name__ == '__main__':
    unittest.main()