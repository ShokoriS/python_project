from pathlib import Path
import logging
import time

# Using logging to save errors expected!
logging.basicConfig(filename="log_document.txt", level=logging.INFO)


class Write:

    @staticmethod
    def writing_improvements():
        """This program will take/ask for everyday improvements and save it in a txt file"""
        path = Path("D:\\programming\\the_result_python_project\\documents.txt")  # the actual path of tasks
        improvement_path = r"D:\\programming\\the_result_python_project\\improvements.txt"  # The path for improvement file
        with (open(path, 'r')) as tasks, open(improvement_path, "a") as improvement_file:

            improvement_file.write(f"\n{time.asctime()}")  # used time.asctime() to indicate the live time and the date

            for task in tasks:  # looping through tasks to get each task and use in improvements file.txt

                improvements = input(f"Would you mind telling me what did you do today in {task} on {time.asctime()}: \n")
                # Asking the user for improvements he made

                improvement_file.write(f"\n in {task} {improvements} \n")  # writing to improvements file

                print()  # printing an empty line

write = Write()

write.writing_improvements()