[![CircleCI](https://circleci.com/gh/OmarThinks/Gemography-Challenge-1.svg?style=svg)](https://circleci.com/gh/OmarThinks/Gemography-Challenge-1)
[![CircleCI Build Status](https://circleci.com/gh/OmarThinks/Gemography-Challenge-1.svg?style=shield "CircleCI Build Status")](https://circleci.com/gh/OmarThinks/Gemography-Challenge-1) 
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/OmarThinks/CircleCI-hello-world/master/LICENSE) 


# Gemography-Challenge-1
Submitting a challenge to Gemography




## Challenge Reference:

<a href="https://github.com/gemography/backend-coding-challenge">
Backend Challenge</a>


## How to run the application:

<b>

```bash
python manage.py runserver
```
</b>


## testing the application using usinttest:

<b>

```bash
python manage.py test
```
</b>



## testing the application using `pytest`:

<b>

```bash
pytest -rP
```

or


```bash
pytest app -rP --junitxml=test-reports/junit.xml --html=test-reports/pytest_report.html --self-contained-html
```

</b>
To print results in HTML file.






# 1) Backend (RESTful API):

The RESTful API has two endpoints:


## (GET) http://127.0.0.1:8000/api/github/search/:

The inputs are passed as query parameters:

- **`order`**: `asc` or `desc`
- **`date`**:
    - It has the format of **`YYYY-MM-DD`**
    - Example: `2019-4-25`
- **`records`**:
    - How many repositories do you want to check
    - Min Value : 1
    - Max Value : 1000

## (POST) http://127.0.0.1:8000/api/github/search/:


The same as the previous, but input is passed in request body.




# Examples:

<img src="images/get_endpoint.gif">


### The date field:

<img src="images/date_field.gif">



### The order field:

<img src="images/order_field.gif">


### Validation:

<img src="images/validation.gif">







# 2) Frontend:


The application has a frontend in this url:  
<a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a> 


The frontend looks like this:


---


<img src="images/frontend_1.png">


---

When submitting the result, it will look like this:



<img src="images/frontend_2.png">

---

<img src="images/frontend_3.png">















# 3) DevOps:

I am learing DevOps.  
The appilaction uses CircleCI.  
Every time commit an update, runs tests.  
And there are file generated by **`pytest`** as CircleCI Artifacts.  
These artifacts contain the results of the tests.








# Todos:


1. More Options when submitting the form, because Github has many more options
2. Add GraphQL
3. Enhance Frontend
4. Communicate with Github GraphQLL API instead of RESTful API
	- Each repository does not have only one language, rather, 
	It uses several languages, when attempting to acess the languages of each repo, 
	we face a problem, that is rate limit, or throttling.
	- So when using the GraphQL API, you will be able to get the languages of 
	each repository, not only the basic language of the repo






































