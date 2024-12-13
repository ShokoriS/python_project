import matplotlib.pyplot as plt
import Write_to_tasks as wt
import logging


def rating():
    fig, ax = plt.subplots()

    rate = []

    while True:
        que = input("do you give your self a positive (+) or a negative (-): ")
        
        with open("rating.txt", "a+") as write_rating, open("rating.txt", "r+") as rating:

            read_rating = rating.read()
            for number in read_rating:
                rate.append(number)
                    
            if que.lower() in {"+", "positive"}:
                rate[-1] = int(rate[-1]) + 1
                write_rating.write(str(rate[-1]))

            elif que.lower() in {"-", "negative"}:
                rate[-1] = int(rate[-1]) + (-1)
                write_rating.write(str(rate[-1]))

        ax.plot(rate)
        plt.show()

        break



try:
    wt.Write.writing_improvements()
    rating()
except (KeyboardInterrupt, EOFError) as ke:
    print("Warning! Please run the program again!")
    logging.info(ke)

except RuntimeError as r:
    print("Warning! Please run the program again! ")
    logging.info(r)

except IndexError as ie:
    logging.info(ie)
