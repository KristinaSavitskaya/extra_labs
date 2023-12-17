import time
import os
from typing import Callable

def execution_time(executed_function: Callable) -> Callable:

    def wrapper(*args):
        time_start = time.time()
        executed_function(*args)
        time_end = time.time()
        execution_time = time_end - time_start
        print(f'Execution time of {executed_function.__name__}: {execution_time:.6f} seconds')
    
    return wrapper

class CommandPrompt:

    def __init__(self):
        self.current_directory = os.getcwd()
        self.is_run = True

    @execution_time
    def show_current_directory(self): # cd 
        print(f'Current directory: {self.current_directory}')

    @execution_time
    def change_directory(self, new_directory): # cd .. 
        try:
            if new_directory == '..':
                os.chdir('../')
                new_directory = os.getcwd()
            else:
                os.chdir(new_directory)
            self.current_directory = new_directory

        except FileNotFoundError:
            print('Системе не удается найти указанный путь.')

        print(self.current_directory)

    @execution_time
    def list_files(self): # dir
        print(f'Содержимое папки {self.current_directory}')
        files = os.listdir(self.current_directory)
        for file in files:
            print(file)

    @execution_time
    def create_folder(self, folder_name): # mkdir
        try:
            os.mkdir(folder_name)
        except FileExistsError:
            print(f'Подпапка или файл {folder_name} уже существует.')


    @execution_time
    def delete_folder(self, folder_name): # rmdir 
        try:
            os.rmdir(folder_name)
        except FileNotFoundError:
            print('Не удается найти указанный файл.')

    @execution_time
    def rename_folder_file(self, old_name, new_name): # rename 
        try: 
            os.rename(old_name, new_name)
        except FileNotFoundError:
            print('Не удается найти указанный файл.')
        except FileExistsError:
            print(f'Подпапка или файл {old_name} уже существует.')


    @execution_time
    def create_file(self, file_name): # type nul > filename
        try:
            with open(os.path.join(self.current_directory, file_name), 'w') as file:
                file.write('')
        except FileExistsError:
            print(f'Подпапка или файл {file_name} уже существует.')


    @execution_time
    def delete_file(self, file_name): # del
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print('Не удается найти указанный файл.')

    @execution_time
    def read_file(self, file_name): # type
        try: 
            with open(os.path.join(self.current_directory, file_name), 'r') as file:
                for line in file.readlines():
                    print(line)
        except FileNotFoundError:
            print('Не удается найти указанный файл.')

    @execution_time
    def run(self):
        while self.is_run:
            user_input = input(f'{self.current_directory}>')
            self.is_run = self.run_commands(user_input)

    def run_commands(self, user_input):
        command = [i for i in user_input.split(' ') if i != '']
        match command[0]:
        
            case "cd":
                if len(command) == 1:
                    self.show_current_directory()
                else:
                    self.change_directory(command[1])

            case "dir":
                self.list_files()

            case "mkdir":
                self.create_folder(command[1])

            case "rmdir":
                self.delete_folder(command[1])

            case "rename":
                self.rename_folder_file(command[1], command[2])

            case "type":
                if command[1][0:3] == 'nul':
                    print(command[-1])
                    self.create_file(command[-1])
                elif len(command) == 2:
                    self.read_file(command[1])

            case "del":
                self.delete_file(command[1])   

            case "exit":
                self.is_run = False

            case _:
                print(f'"{command}" не является внутренней или внешней\nкомандой, исполняемой программой или пакетным файлом.')

        return self.is_run

    
cmd = CommandPrompt()
cmd.run()
