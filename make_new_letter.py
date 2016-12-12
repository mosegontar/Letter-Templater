#!/home/math1/agontar/Desktop/personal/LetTemp/venv/bin/python
import argparse
import os
import re

class LetterTemplate(object):

    def __init__(self):
        
        self.cwd = os.getcwd()
        self.template_files = [f for f in os.listdir(self.cwd) if f.startswith('lettemp')]
        self.template_name = ''
        self.content = ''
        self.placeholders = []
        self.new_letter = ''
        self.new_directory = ''

    def get_template_text(self):

        if len(self.template_files) != 1:        
            for index, name in enumerate(self.template_files):
                print '[%d] %s' % (index+1, name)
            choice = raw_input('Select a template: ')

            self.template_name = self.template_files[int(choice) - 1]
        else:
            self.template_name = self.template_files[0]

        with open(self.template_name, 'r') as f:
            self.content = f.read()

        self.placeholders = re.findall(r'\{\{ \w+ \}\}', self.content)

    def replace_placeholders(self, **kwargs):

        self.new_letter = self.content
        
        for ph in self.placeholders:

            ph_name = ph.split(' ')[1].strip()

            value = kwargs.get(ph_name)
            if not value:
                value = raw_input(ph_name+': ')

            self.new_letter = self.new_letter.replace(ph, value)

    def make_new_directory(self, directory_name):
        self.new_directory = os.getcwd()+'/'+directory_name
        if not os.path.exists(self.new_directory):
            os.makedirs(self.new_directory)

    def save_new_letter(self, filename=None, new_directory=True):

        if not filename:
            filename = raw_input('Save as? ')

        full_path = os.getcwd()+'/'+filename
        if new_directory:
            new_directory_name = raw_input('Directory name: ')
            self.make_new_directory(new_directory_name)
            full_path = os.getcwd()+'/'+new_directory_name+'/'+filename

        with open(full_path, 'w') as new_letter_file:
            new_letter_file.write(self.new_letter)
            new_letter_file.close()

if __name__ == '__main__':

    letter = LetterTemplate()
    letter.get_template_text()
    letter.replace_placeholders()
    letter.save_new_letter()
