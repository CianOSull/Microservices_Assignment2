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
    # Total amount of posts removed in the last 3 minutes
    # removed_count = 0
    # Total number of over 18
    # over_count = 0

    # New metrics
    # The highest score and title of post
    highest_score = 0
    highest_score_title = ""
    # The highest total comments and title of post
    highest_comments = 0
    highest_comments_title = ""

    # Counter for tracking metrics
    counter = 0

    # Time Count
    start = time.time()
    extra = False

    with grpc.insecure_channel('serverred:50052') as channel:
        stub = data_pb2_grpc.GetDataServiceStub(channel)

        for data in data_reader.get_posts():
            data_split = data.split(" @ ")
            # Last index is always empty so remove it
            data_split.pop(-1)

            for post in data_split:
                metrics = "<br>"

                post_info = post.split(",")

                # if 12 < len(post_info):
                #     diff = len(post_info) - 12

                #     for i in range(diff):
                #         post_info[1] += "," + post_info[2]
                #         post_info.pop(2)

                if len(post_info) != 12:
                    continue

                counter += 1

                # # Metric number 2
                # if post_info[5] != "":
                #     removed_count += 1

                # # Metric number 4
                # if post_info[11] == 'True\n':
                #     over_count += 1
                
                # Metric Highest score
                if highest_score < int(post_info[2]):
                    highest_score = int(post_info[2])
                    highest_score_title = post_info[1]

                # Metric Highest awards
                if highest_comments < int(post_info[10]):
                    highest_comments = int(post_info[10])
                    highest_comments_title = post_info[1]


                # Reddit stat section
                metrics += "=============================<br>"
                metrics += "Reddit Metrics #:" + str(counter) + ":" + "<br>"
                metrics += "=============================<br>"

                # Time that has passed
                # metrics += "=============================<br>"
                metrics += "Time counter: " + str((time.time() - start)) + "<br>"
                metrics += "=============================<br>"

                # # Metric 2 
                # metrics += "Number of removed posts: " + str(removed_count) + "<br>"
                # metrics += "=============================<br>"

                # # Metric 4
                # metrics += "Over 18 count: " + str(over_count) + "<br>"
                # metrics += "=============================<br>"

                # Metric highest score
                metrics += "Highest score: " + str(highest_score) + "<br>"
                metrics += "Title of Highest Score:" + highest_score_title + "<br>"
                metrics += "=============================<br>"

                # Metric Hightest comments
                metrics += "Highest comments total: " + str(highest_comments) + "<br>"
                metrics += "Title of Highest comments total:" + highest_comments_title + "<br>"
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