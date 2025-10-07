import sys;
from stats import count_words, count_chars, build_report;

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read();

def main():
    sys_args = sys.argv;
    if(len(sys_args) < 2):
        print("Usage: python3 main.py <path_to_book>");
        sys.exit(1);
    
    file_content = get_book_text(sys_args[1]);
    build_report(count_words(file_content), count_chars(file_content));

main();