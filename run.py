from server import app   #imports the app from server folder __init__

## server inititaion and declaration ##
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
