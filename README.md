## Todo App with Python and Flask

This is a simple todo app that allows users to add, edit, and delete tasks. The app is built using the Flask web framework and uses a simple in-memory data store to store the list of tasks.

### Functionality

The app allows users to perform the following actions:

- Add a new task to the list
- View the list of tasks
- Edit an existing task in the list
- Delete an existing task from the list

### Installation

To run the app, you will need to have Python and Flask installed on your machine. You can install Flask using pip by running the following command:

```
pip install flask
```

### Running the App

To run the app, navigate to the directory where the `app.py` file is located and run the following command:

```
python app.py
```

This will start the Flask development server, which will host the app on `http://localhost:5000/`.

### File Structure

The app is organized into two main directories:

- `templates`: contains the HTML templates for the app

The main Python file (`app.py`) contains the code for the Flask app, including the route definitions and the logic for adding, editing, and deleting tasks.

### Resources

If you're new to Flask, here are some resources that you may find helpful:

- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
