# Dr.Diagno
#### Dr.Diagno is an Artificial Intelligence based app which predicts the diseases or other health conditions based on the provided symptoms.
---
##### How Dr.Diagno works:
1. Initially,the user is prompted to create an account. This helps in keeping track of the user's past predictions and some other vital information.
2. The next page requests for the information which the app requires to carry out the diagnostic, which are Sympotoms, temperature and the number of days the user has been experiencing the symptoms.
3. The data given by the user is transfered to the backend(django) which contains the MachineLearning models that predict and return the most possible diseases to the app.
4. The app then generates a graph that depicts the results processsed by the MachineLearning models.
5. After the prediction phase, details like the disease description and the appropriate precautions are loaded onto the home screen, so that the user can get a few more insights about his condition.

---

### Tech Stack
* Front-End: React, Chart.js, Material UI
* Back-End: Django Rest Framework, JSON Web Token(JWT)
* Database: PostGreSQL
* AI: Catboost Algorithm from Catboost package

---
### How to run this app:
1. Clone this repository
```
git clone https://github.com/GanapathyPT/Dr.Diagno_Backend.git
```
2. change the directory
```
cd Dr.Diagno_Backend
```
3. Initialize local environment
```
python3 -m venv venv
source venv/bin/activate
```
4. Intall the requirements
```
pip3 install -r requirements.txt
```
5.Make migrations 
```
python3 manage.py makemigrations
python3 manage.py migrate
```
6. Run Server
```
python3 manage.py runserver
```
7. The app will run on the localhost:8000
