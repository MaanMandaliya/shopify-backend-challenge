from inventory import app

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True, port=8080, threaded=False)
