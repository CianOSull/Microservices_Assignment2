from random import randint

# Bascially a function to  get some quick metrics
def metrics(event, context):
  # Decide whcih files to get metrics out of
  metric_choice = event['data']
  
  # For deciding what metrics to get
  get_reddit = False
  get_youtube = False

  if metric_choice == "b" or metric_choice == "Both" or metric_choice == "both":
      get_reddit = True
      get_youtube = True
  elif metric_choice == "r" or metric_choice == "Reddit" or metric_choice == "reddit":
      get_reddit = True
  elif metric_choice == "y" or metric_choice == "Youtube" or metric_choice == "youtube":
      get_youtube = True

  if get_reddit:
    reddit_csv = open("../ClientRed/r_dataisbeautiful_posts.csv")

    reddit_csv_lines = reddit_csv.readlines()

    # Pop the headings
    reddit_csv_lines.pop(0)

    # This will be the output string
    metrics = ""
    
    # Get 5 random lines from reddit
    counter = 0
    # The highest score and title of post
    highest_score = 0
    highest_score_title = ""
    # The highest total comments and title of post
    highest_comments = 0
    highest_comments_title = ""

    while(counter < 5):
      line = reddit_csv_lines[randint(0, len(reddit_csv_lines))]

      post_info = line.split(",")

      # If a line is 
      if len(post_info) != 12:
        continue

      else:
        counter += 1

      # Metric Highest score
      if highest_score < int(post_info[2]):
          highest_score = int(post_info[2])
          highest_score_title = post_info[1]

      # Metric Highest awards
      if highest_comments < int(post_info[10]):
          highest_comments = int(post_info[10])
          highest_comments_title = post_info[1]

    # Metric highest score
    metrics += "Highest score: " + str(highest_score) + "\n"
    metrics += "Title of Highest Score:" + highest_score_title + "\n"
    metrics += "=============================\n"

    # Metric Hightest comments
    metrics += "Highest comments total: " + str(highest_comments) + "\n"
    metrics += "Title of Highest comments total:" + highest_comments_title + "\n"
    metrics += "=============================\n"

  # Now do youtube metrics
  if get_youtube:
    youtube_csv = open("../ClientYou/GBvideos.csv")

    youtube_csv_lines = youtube_csv.readlines()

    youtube_csv_lines.pop(0)

    counter = 0
    # Highest likes
    highest_likes = 0
    highest_likes_title = ""

    # Highest comment count
    highest_comment_count = 0
    highest_comment_count_title = ""

    while(counter < 5):
      line = youtube_csv_lines[randint(0, len(youtube_csv_lines))]

      post_info = line.split(",")

      # If a line is 
      if len(post_info) != 16:
        continue

      else:
        counter += 1

      # Metric Highest likes
      if highest_likes < int(post_info[8]):
          highest_likes = int(post_info[8])
          highest_likes_title = post_info[2]

      # Metric Highest comment count
      if highest_comment_count < int(post_info[10]):
          highest_comment_count = int(post_info[10])
          highest_comment_count_title = post_info[2]
      
     # Metric Highest likes 
    metrics += "Highest likes: " + str(highest_likes) + "\n"
    metrics += "Title of Highest likes:" + highest_likes_title + "\n"
    metrics += "=============================\n"

    # Metric Highest comment count
    metrics += "Highest comments total: " + str(highest_comment_count) + "\n"
    metrics += "Title of Highest comments total:" + highest_comment_count_title + "\n"
    metrics += "=============================\n"

  return metrics

# Uncomment this to run this file through python
# event = {'data' : 'both'}
# print(metrics(event, None))