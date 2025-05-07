from app import create_app

app = create_app()
app.secret_key = 'secret_key_for_flask_session'

if __name__ == "__main__":
    app.run(debug=True, port=5001)
