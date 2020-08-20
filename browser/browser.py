import sys
import os
import requests

from bs4 import BeautifulSoup
from colorama import Fore


class Browser:
    def __init__(self):
        self.input_url = ""
        self.urls_storage = []
        self.history_urls = []
        self.directory = ""
        self.create_directory()
        self.result()

    def result(self):
        self.input_url = input()
        while self.input_url != "exit":
            if self.input_url in self.urls_storage:
                self.storage_directory()
            elif '.' in self.input_url:
                self.webpage_search()
            elif self.input_url == "back":
                self.history_search()
            else:
                print("Error: Incorrect URL")
            self.input_url = input()

    def create_directory(self):
        input_argv = sys.argv
        if len(input_argv) != 2:
            print(
                "Must enter command 'python browser.py [directory name]' in that format - directory name is the directory to save to ")
            quit()
        self.directory = input_argv[1]
        os.makedirs(self.directory, exist_ok=True)

    def storage_directory(self):
        with open(self.directory + "/" + self.input_url, 'r') as f_in:
            print(f_in.read())
        self.history_urls.append(self.input_url)

    def webpage_search(self):
        self.urls_storage.append(self.input_url)
        self.history_urls.append(self.input_url)
        r = requests.get("https://" + self.input_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        result = soup.find_all(['p', 'a', 'ul', 'ol', 'li'])
        with open(self.directory + "/" + self.input_url, 'w') as f_out:
            for i in result:
                if i == 'a':
                    f_out.write(Fore.BLUE + i.text)
                    print(Fore.BLUE + i.text)
                else:
                    f_out.write(Fore.BLUE + i.text)
                    print(Fore.BLUE + i.text)

    def history_search(self):
        self.history_urls.pop()
        if len(self.history_urls) != 0:
            with open(self.directory + "/" + self.history_urls[-1], 'r') as f_in:
                print(f_in.read())


if __name__ == "__main__":
    Browser()
