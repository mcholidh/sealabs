from flask import Flask, request

app = Flask(__name__)

# create a dictionary to keep track of user IPs and hit count
users = {}

@app.route('/')
def index():
    # get the user's IP address
    user_ip = request.remote_addr
    
    # increment the hit count for this IP address
    if user_ip in users:
        users[user_ip] += 1
    else:
        users[user_ip] = 1
    
    # print the user's IP address and hit count
    return f"User Address: {user_ip}  <-- user ip was set to {user_ip} "
    return f"Hits: {users[user_ip]}"

if __name__ == "__main__":
    app.run(host="0.0.0.0")