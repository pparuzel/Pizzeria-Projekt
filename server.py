from python.flask.routes import *


if __name__ == '__main__':
    # db.drop_all()
    db.create_all()
    setup_admin_view()
    app.run(
        host='localhost',
        port=5000,
        debug=True
    )
