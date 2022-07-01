from app import app
from app.controllers import User



print("inside server file")

if __name__=="__main__":
	print("SERVER FILE")
	app.run(debug=True)
	