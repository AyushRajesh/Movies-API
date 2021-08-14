# Movies-API
REST API to Insert, Update, Delete and Retrieve the Movie name, actor, actress, year of release and director of the movie.

## What is a Rest API?

- A RESTful API uses HTTP  requests to GET, PUT, POST, DELETE data the following the REST standards.
- This allows two pieces of software to communicate with each other.

## REST API example application

1. This is a bare_bones example of a movies application providing a REST API to a database.
2. The entire application is contained within the **movies.py** file.
3. **movies.sql** is the database stored for the entire Application.
4. We have used the **MYSQL DATABASE**.
5. We have used **Postman** which is a scalable API testing tool to test API.

### Paths
 A good RESTful design has a pattern for the URL, such that:
- GET:/movies- Returns an arrary of "movie" record.
- GET:/movie/id- Gets a specific "movie" record.
- PUT:/movie/id- Updates a specific "movie" record.
- POST:/movies/- Creates a new "movie" record.
- DELETE:/movies/id-Deletes a "movie" record.

### Response Codes
The more detail the better here, but if I at least hear:
- **200**- Success.
- **201**- Created.
- **300**- Proxies handle it.
- **400**- Error.
- **401**- Not Authorized.
- **404**- Not found.
- **500**- Internal Server Error.
- and more on [https://www.restapitutorial.com/httpstatuscodes.html]()

# About Project

I have created a REST API which retrieve, update, delete, create  movie records in the book database. Movie records contains name of movie, actor, actress, year of release, director of the movie. We use request methods such as GET, POST, PUT, DELETE to perform operations on the book records stored in the database by HTTP Response. I have made this entire project in Python using Flask and MYSQL Database.

## Run install

To run the API, we need to install some module
- First of all, Create a folder then open the folder and write the following command in command prompt to create virtual environment.
 ```PYTHON
 python -m venv venv
 ```
 - Now, open the script folder in venv folder then copy paste the activate file in command prompt and press enter.
 - Now it's time to download the modules which we are going to use in program code. 
 - To install **Flask** open the command prompt and write the command:-
  ```PYTHON
 pip install flask
 ```
 - Here we have used the **MYSQL** database in python. So, to install **Pymysql** open the command prompt and write the command:-
  ```PYTHON
 pip install Pymysql
 ```
 ## RUN movies
 
  ```PYTHON
 python movies.py
 ```
After running the program we get
``` PYTHON
* Serving Flask app 'movies' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 107-463-888
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Just copy the http://127.0.0.1:5000/ and run it in the browser or in the postman app to test the different methods.

# Get list of movies

## Request
```PYTHON
GET/movies/
```

```PYTHON
http://127.0.0.1:5000/movies
```
## Response

```PYTHON
127.0.0.1 - - [19/Jun/2021 14:44:22] "GET /movies HTTP/1.1" 200 -
```
```PYTHON
[
  {
   "Name": "Radhe",
   "Actor": "Salman Khan",
   "Actress": "Disha Patni",
   "Year": "2021",
   "Director": "Prabhu Deva",
   "id": 1
  }, 
  {
    "Name": "DDLJ",
    "Actor": "Shahruk Khan",
    "Actress": "Kajol Devgan",
    "Year": "1995",
    "Director": "Aditya Chopra",
    "id": 2
  }, 
  {
    "Name": "Hum Aapke Hain Koun",
    "Actor": "Salman Khan",
    "Actress": "Madhuri Dixit",
    "Year": "1994",
    "Director": "Sooraj Barjatya",
    "id": 3
  },
  {
    "Name": "Chhichhore",
    "Actor": "Sushant Singh Rajput",
    "Actress": "Shraddha Kapoor",
    "Year": "2019",
    "Director": "Nitesh Tiwari",
    "id": 6
  }
  ]
```

# Create a new movie

## Request
```PYTHON
POST/movies/
```

```PYTHON
http://127.0.0.1:5000/movies
```
## Response

```PYTHON
127.0.0.1 - - [19/Jun/2021 14:50:26] "POST /movies HTTP/1.1" 200 -
```
```PYTHON
movies details created successfully
```

# Get a specific movie record

## Request
```PYTHON
GET/movie/id
```

```PYTHON
http://127.0.0.1:5000/movie/2
```
## Response

```PYTHON
127.0.0.1 - - [19/Jun/2021 14:50:26] "GET/movie/2 HTTP/1.1" 200 -
```
```PYTHON
{
    "Name": "DDLJ",
    "Actor": "Shahruk Khan",
    "Actress": "Kajol Devgan",
    "Year": "1995",
    "Director": "Aditya Chopra",
    "id": 2
}
```

# Get a non-existent movie

## Request
```PYTHON
GET/movie/id
```

```PYTHON
http://127.0.0.1:5000/movie/14
```
## Response

```PYTHON
127.0.0.1 - - [19/Jun/2021 14:54:46] "GET /movie/14 HTTP/1.1" 404 -
```
```PYTHON
No movie found for this id.
```

# Change a movie's state

## Request
```PYTHON
PUT/movie/id
```

```PYTHON
http://127.0.0.1:5000/movie/3
```
## Response

```PYTHON
127.0.0.1 - - [19/Jun/2021 14:54:47] "PUT /movie/3 HTTP/1.1" 200 -
```
```PYTHON
Movie with id 3 has been updated successfully
```

# Delete a Movie

## Request
```PYTHON
DELETE/movie/id
```

```PYTHON
http://127.0.0.1:5000/movie/4
```
## Response

```PYTHON
127.0.0.1 - - [19/Jun/2021 14:54:47] "DELETE /movie/4 HTTP/1.1" 200 -
```
```PYTHON
The movie with id: 4 has been deleted.
```
