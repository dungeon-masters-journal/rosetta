import re
import string
from PIL import Image
from typing import List

def clean_text(text_line: str) -> string: 
    ''' Cleans up the string so only a-z and 0-9 characters are available '''

    lower_case_str = text_line.lower()
    no_punc_str = lower_case_str.translate(str.maketrans('', '', string.punctuation))
    no_emoji_str = remove_emojis(no_punc_str)
    no_url_str = re.sub(r'^https?:\/\/.*[\r\n]*', '', no_emoji_str, flags=re.MULTILINE)
    no_email_str = re.sub(r'\S*@\S*\s?', '', no_url_str)
    no_space_str = no_email_str.replace(" ", "")
    stripped_str = no_space_str.strip()

    return stripped_str

def remove_emojis(text: str) -> string:
    '''
    Removes Emoji characters
    https://stackoverflow.com/questions/33404752/removing-emojis-from-a-string-in-python"
    '''

    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

def merge_lines(line_counter: int):
    ''' For multi-line messages, combines them into a single JPG'''
    y_offset = 0
    line_list = [f'images/output/output_{i}.jpg' for i in range(1, line_counter + 1)]
    
    images = [Image.open(x) for x in line_list]
    widths, heights = zip(*(i.size for i in images))
    
    max_width = max(widths)
    total_height = sum(heights)
    
    new_im = Image.new(mode = 'RGB', size = (max_width, total_height), color=(255,255,255))

    for im in images:
        new_im.paste(im, (0, y_offset))
        y_offset += im.size[1]

    new_im.save('images/output/final.jpg')

def read_file(input_file: str) -> List:
    with open(input_file, "r") as original_text:
        lines = original_text.readlines()
    return lines

def translate(letters: list, line_counter: int):
    x_offset = 0
    letter_list = []
    images = []

    letter_list = [f'images/symbols/{l}.jpg' for l in letters]
    images = [Image.open(x) for x in letter_list]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new(mode = 'RGB', size = (total_width, max_height), color=(255,255,255))
    
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]
    
    new_im.save(f'images/output/output_{line_counter}.jpg')

def main(input_file: str):
    input_txt = read_file(input_file)
    line_counter = 0
 
    for input_line in input_txt:
        line_counter +=1
        clean_line = clean_text(input_line)
        translate(clean_line, line_counter)

    merge_lines(line_counter)

if __name__ == "__main__":
    input_file = "input.txt"
    main(input_file)
