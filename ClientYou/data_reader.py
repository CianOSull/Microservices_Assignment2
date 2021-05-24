from random import randint
import time
import codecs

def get_posts():
    # data = open("Client/r_dataisbeautiful_posts.csv")
    data_input_stream = codecs.open("ClientYou/GBvideos.csv", "r", encoding='utf-8')

    file_lines = data_input_stream.readlines()

    # The first line of the file is the headings
    # id, title, score, author, author_flair_text, removed_by, total_awards_received, awarders, created_utc, full_link, num_comments,over_18
    headings = file_lines.pop(0)

    size_of_data = len(file_lines)
    
    # Get the amount of posts that was streamed in
    for i in range(size_of_data):
        # Defines how many posts to send
        # num_of_posts = randint(2,10)
        num_of_posts = 50

        message = ""

        # Get the amount of posts that was streamed in
        for j in range(num_of_posts):
            # Take random posts from the dataset
            line = file_lines[randint(0, size_of_data)]

            # If the line is empty then just keep going
            if len(line) == 0:
                continue

            # Construct the message string
            message += line + " @ "
        
        # message += "_" + str(i)

        yield message

        time.sleep(20)
    
    data.close()
