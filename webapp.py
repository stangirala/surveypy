from flask import Flask

app = Flask(__name__)

@app.route('/')
def unknown():
  return "Well, this is embarrring. You don't follow instructions."

@app.route('/pushsurvey', methods=['POST'])
def pushsurvey():
  if request.method == 'POST':
    return request.json
  else:
    return abort(405)

if __name__ == '__main__':
  app.run()
