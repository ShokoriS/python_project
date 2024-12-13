from pathlib import Path
import sys
import logging
import time

logging.basicConfig(filename='log_document.txt', level=logging.INFO)


class GetTasks:
    
    def __init__(self):
        self.que = None
        self.number_of_tasks_ls = None

    def get_number_of_tasks(self):
        que = input("Do you want to Add tasks to existing ones or create new tasks\n"
                    "Enter (1) for Creating and (2) for adding to existing tasks: ")
        self.que = que

        number_of_tasks = None
        chances = 3
        while number_of_tasks is None:
            if chances < 1:
                print("The program didn't get any integers, please run the program again!")
                sys.exit()
            try:
                number_of_tasks = int(input("Number of the tasks: "))
                if number_of_tasks <= 0:
                    print("Please enter an integer bigger than (0)!\n")
                    number_of_tasks = None

            except ValueError as v:
                print("Please enter an integer!\n")
                chances -= 1
                logging.info(v)

            except (KeyboardInterrupt, EOFError) as key0:
                print("\nError occurred! Please enter the information again!\n")
                logging.info(key0)

        self.number_of_tasks_ls = [input("Please enter your task: ") for _ in range(number_of_tasks)]
    
    def storing_tasks(self):
        """The func will save the tasks in a .txt file for later use."""
        contents = ".\n".join(self.number_of_tasks_ls) + "\n"
        path = Path("documents.txt")

        mode = 'w' if self.que == '1' else 'a'
        with open(path, mode) as task_file:
            task_file.write(contents)


try:
    tasks = GetTasks()
    tasks.get_number_of_tasks()
    tasks.storing_tasks()
except ValueError as ve:
    print("\n!Warning, an Error occurred! \nPlease run the program again!")
    logging.exception(ve)
except TypeError as te:
    print("\n!Warning, an error occurred!\nPlease run the program again!")
    logging.exception(te)
except (KeyboardInterrupt, EOFError) as ke:
    logging.exception(ke)
except FileNotFoundError as ffe:
    print("Please make sure you are indicating to a real file directory 'while saving your tasks'.")
    logging.exception(ffe)
except AttributeError as ae:
    logging.exception(ae)

else:
    def loading():
        for _ in range(10):
            time.sleep(0.2)
            yield "."
    
    print("Checking", end="")
    for dot in loading():
        print(dot, end="", flush=True)

    time.sleep(1.5)
    print("\n\nYou sure you didn't make a mistake?")
    time.sleep(0.5)
    print("If you did, please run the program again or you can find the documents.txt file \nin your computer and "
          "make changes directly!")
