# Deploy Machine Learning Model use Iris Dataset Input from Webform 

This is simple project to implement machine learning model with flask in python.

## Development setup

To get started, you'll want to install the dependencies for this project.

1. This project uses `pipenv` to handle dependencies and virtual environments. To get started, make sure you have [`pipenv` installed](https://github.com/kennethreitz/pipenv#installation).

2. With `pipenv` installed, make sure you have the `all-the-places` repository checked out

   ```
   git clone git@github.com:YudhaBhakti95/Deploy-Machine-Learning-Model-Iris.git
   ```

3. Then you can install the dependencies for the project

   ```
   cd Deploy-Machine-Learning-Model-Iris
   pipenv install
   ```

4. After dependencies are installed, make sure you can run the shell command without error

   ```
   pipenv shell
   ```
## Start
This project is running on localhost with port 5000 for API and 5001 for webform.To run this project, you must run two python file webforms.py and server.py. Webforms.py is webservice to input your Iris prediction data and get output from API. Server.py is API to run model and give return the output.
1. python webforms.py & server.py
2. check your localhost:5001 on your web browser
![alt text](https://i.imgur.com/CtYDYlk.png)
3. to change the model and use different dataset, you can edit on file model.py
