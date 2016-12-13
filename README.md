# Letter-Templater

## Usage
`make_new_letter.py` will identify all template files in your current working directory.

Template files begin with "lettemp_". If a directory has more than one template file, you will be prompted to select one from a list.

Templates (inspired by Jinja2) look like this:
> Dear {{ NAME }},
> 
> We are happy to announce your admittance into {{ SOME_SCHOOL_OF_WITCHCRAFT_AND_WIZARDY }}
> 
> Please Venmo your tution to {{ EMAIL }}
> 
> Sincerely,
> Professor {{ WIZARD }}

`make_new_letter.py` will then prompt the user with the various items found between {{ }}, and the user will supply the proper replacement values.

The user will also be asked to supply a filename for the new letter, and a directory name, which will be a newly created subdirectory of the current working directory. This subdirectory will house the new letter.

