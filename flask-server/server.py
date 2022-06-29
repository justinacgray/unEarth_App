from flask_app import create_app
# from flask_app.controllers import user_controller, search_controller

app = create_app()

if __name__=="__main__":
	app.run(debug=True)