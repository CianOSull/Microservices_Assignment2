# Says if you want to see more about this, go to:
# http://flask.pocoo.org

from flask import Flask

import redis

app = Flask(__name__)

@app.route('/')
def print_logs():
    output = ''
    try:
        conn = redis.StrictRedis(host='redis', port=6379)
        for key in conn.scan_iter("Post_Info:*"):
            value = str(conn.get(key))
            # output += str(key) + value + '<br>'
            # Removing key as it probably doesn't need to be outputted
            output += value + '<br>'
    except Exception as ex:
        output = 'Error:' + str(ex)
    return output

@app.route('/GetPosts/', methods=['GET'])
def get_time():
    # output = 'COME ON BABY JSUT WORK DAMMIT'
    output = ''
    output_dict = {}
    # output_dict["time"] = output

    try:
        conn = redis.StrictRedis(host='redis', port=6379)

        # Set up metrics
        for key in conn.scan_iter("Post_Info:*"):
            value = conn.get(key).decode('utf-8')
            output += value
        
        output_dict["posts"] = output

    except Exception as ex:
        output = 'Error:' + str(ex)

    return output_dict, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')