# runs and creates the app
# importing __init__.py from website, and running the create app function

from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)