# [DMs Journal](www.dmsjournal.blog)

## Rosetta

### Table of Contents

- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Setup](#setup)
- [Using the Program](#using-the-program)

### Buy me a coffee

Whether you use this project, have learned something from it, or just like it, please consider supporting it by buying me a coffee, so I can dedicate more time on open-source projects like this.

<a href="https://www.buymeacoffee.com/dmsjournal" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

### Introduction

Rosetta is a simple project which takes an input from a text file and converts it to fictional languages. This project was built to assist in the conversion to the Abyssal rune language for a DnD campaign and as such that is the only available language at the moment.

### Setup

```bash
git clone https://github.com/DMs-Journal/rosetta.git
cd rosetta
docker-compose build
```

### Using the Program

Put the message you want to translate in `input.txt`. This program only supports English.

```bash
docker-compose run translate
```

### Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request
- Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue here](https://github.com/DMs-Journal/rosetta/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an [issue here](https://github.com/DMs-Journal/rosetta/issues/new). Please include sample queries and their corresponding results.
