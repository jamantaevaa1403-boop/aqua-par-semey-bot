from flask import Flask
import of
app = Flask(_name_)
@app.route('/')
def index():
  return "✅️ Aqua par Semey bot is running!"
  if _name_ == '_main_':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
