from todo_list import create_app

# should we import flask
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    
    
