init:
	./Scripts/Activate.ps1
run:
	$Env:FLASK_APP="app/main.py"
	flask --app app.main run