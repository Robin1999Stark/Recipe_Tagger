from nltk.tokenize import sent_tokenize
import os
import nltk
import re


nltk.download('punkt')


def remove_brackets(text):
    return re.sub(r'\[.*?\]', '', text)


def process_files(input_folder, output_file):
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for filename in os.listdir(input_folder):
            if filename.endswith('.txt'):
                file_path = os.path.join(input_folder, filename)
                with open(file_path, 'r', encoding='utf-8') as in_file:
                    text = in_file.read()
                    text_without_brackets = remove_brackets(text)
                    sentences = sent_tokenize(text_without_brackets)
                    for sentence in sentences:
                        out_file.write(sentence + '\n')


if __name__ == "__main__":
    # Replace with the path to your input folder
    input_folder_path = "./files"
    # Replace with the desired output file path
    output_file_path = "all_recipes.txt"

    process_files(input_folder_path, output_file_path)
