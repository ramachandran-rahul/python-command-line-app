Language Tool CLI
=================

Overview
--------

The Language Tool CLI is a Python-based command-line application developed as part of the UNIX Systems Programming course at the University of Technology Sydney. It facilitates the querying of language data from text files, providing functionalities such as listing languages, searching by ISO codes, and filtering by character sets.

Features
--------

-   List Languages (`-a`): Displays all language names from the file in alphabetical order.
-   Search by ISO Code (`-c [code]`): Finds a language based on its two-character ISO code.
-   Filter by Character Set (`-s [set]`): Lists languages that match a specific character set.
-   View Submission Details (`-v`): Shows the author's credentials and submission details for academic transparency.

Usage and Expected Outputs
--------------------------

Use the script from the command line by specifying an option and the argument file:


###List all languages in alphabetical order

python languages.py -a argument_file

**Output:** Languages in this file: Chinese, English, German, Hindi, Italian, Japanese, Korean, Vietnamese


###Search for a language by ISO code

python languages.py -c 'it' argument_file

**Output:** Italian


###Filter languages by character set

python languages.py -s 'ISO-8859-1' argument_file

**Output:** German, English, Italian


###View author credentials (requires argument file but does not use it)

python languages.py -v argument_file

**Output:** [Your Name, Student ID, Date of Completion]


**Note:** The `argument_file` parameter in these examples should be replaced with the actual file name containing the language data.

Error Handling
--------------

The CLI includes robust error handling for file accessibility and argument validation, ensuring clear feedback is provided for issues like non-existent, unreadable, or improperly formatted files.

Contributing
------------

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.
