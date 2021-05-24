import os
import grpc
import time
import data_pb2
import data_pb2_grpc
from random import randint

import logging

import data_reader


def run():
    # Store information from the file
    # # Metric 1
    # you_total_comments_disabled = 0
    # # Metric 2
    # you_total_ratings_disabled = 0

    # Highest likes
    highest_likes = 0
    highest_likes_title = ""

    # Highest comment count
    highest_comment_count = 0
    highest_comment_count_title = ""

    # Counter for tracking metrics
    counter = 0

    # Time Count
    start = time.time()
    extra = False

    with grpc.insecure_channel('serveryou:50051') as channel:
        stub = data_pb2_grpc.GetDataServiceStub(channel)

        for data in data_reader.get_posts():
            data_split = data.split(" @ ")
            # Last index is always empty so remove it
            data_split.pop(-1)

            for post in data_split:
                metrics = "<br>"

                post_info = post.split(",")

                # Splits that are under or over 16 can break so limit them
                if len(post_info) != 16:
                    continue
                
                else:
                    counter += 1

                # # Metric number 1
                # if post_info[12] == "True":
                #     you_total_comments_disabled += 1

                # # Metric number 2
                # if post_info[13] == "True":
                #     you_total_ratings_disabled += 1

                # Metric Highest likes
                if highest_likes < int(post_info[8]):
                    highest_likes = int(post_info[8])
                    highest_likes_title = post_info[2]

                # Metric Highest comment count
                if highest_comment_count < int(post_info[10]):
                    highest_comment_count = int(post_info[10])
                    highest_comment_count_title = post_info[2]

                # Reddit stat section
                metrics += "=============================<br>"
                metrics += "Youtube Metrics #" + str(counter) + ":" + "<br>"
                metrics += "=============================<br>"

                # Time that has passed
                metrics += "Time counter: " + str((time.time() - start)) + "<br>"
                metrics += "=============================<br>"

                # # Metric 2 
                # metrics += "Number of Videos with comments disabled: " + str(you_total_comments_disabled) + "<br>"
                # metrics += "=============================<br>"

                # # Metric 4
                # metrics += "Number of Videos with ratings disabled: " + str(you_total_ratings_disabled) + "<br>"
                # metrics += "=============================<br>"

                # Metric Highest likes 
                metrics += "Highest likes: " + str(highest_likes) + "<br>"
                metrics += "Title of Highest likes:" + highest_likes_title + "<br>"
                metrics += "=============================<br>"

                # Metric Highest comment count
                metrics += "Highest comments total: " + str(highest_comment_count) + "<br>"
                metrics += "Title of Highest comments total:" + highest_comment_count_title + "<br>"
                metrics += "=============================<br>"

                response = stub.GetData(data_pb2.Posts(posts=metrics))

            # response = stub.GetData(data_pb2.Posts(posts="Passed in String"))
            # response = stub.GetData(data_pb2.Posts(posts=str(data_posts)))

        print("Client.py: ", response.received)
        # time.sleep(randint(1, 6))
        time.sleep(120)


if __name__ == "__main__":
    logging.basicConfig()
    run()