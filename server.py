import os
from python.flask.routes import *

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='localhost', port=port, debug=True)