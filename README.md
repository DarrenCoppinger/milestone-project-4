[![Build Status](https://travis-ci.org/DarrenCoppinger/milestone-project-4.svg?branch=master)](https://travis-ci.org/DarrenCoppinger/milestone-project-4)

# BarTender - Milestone 4 Project

![BarTender Project Image](https://i.ibb.co/s6J6dMv/bartender-banner.jpg)

##[Deployed BarTender website here](https://bartender-ms4.herokuapp.com/)

---

## Introduction
This website, [BarTender](https://bartender-ms4.herokuapp.com/), is an online tool for customers of a bar who:
- wish to book a seat for a particular date and time
- order drinks to a seat in a completely contactless way

## Table of Contents
0. [**Introduction**](#introduction)
1. [**UX**](#ux)
    - [**Design Objectives**](#design-objectives)
        - [**Appropriate for Audience**](#appropriate-for-audience)
        - [**Content Relavence and Accuracy**](#content-relevence-and-accuracy)
        - [**Content Grouping**](#content-grouping)
        - [**Technology**](#technology)
    - [**User stories**](#user-tories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Colors**](#colors)
        - [**Icons**](#icons)
        - [**Typography**](#typography)
    - [**Wireframe**](#wireframe)
2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
        - [**All Pages**](#all-pages)
        - [**Home**](#home)
        - [**Drinks**](#drinks)
        - [**Booking**](#booking)
        - [**Cart**](#cart)
        - [**Checkout**](#checkout)
        - [**Search**](#search)
        - [**Login**](#login)
        - [**Registration**](#registration)
    - [**Features Left to Implement**](#features-left-to-implement)
3. [**Technologies Used**](#technologies-used)
    - [**Frontend Technologies**](#frontend-technologies)
    - [**Backend Technologies**](#Backend-technologies)

4. [**Testing**](#testing)
    - [**Code Validators**](#code-validators)
        - [**WC3 Markup Validator**](#w3c-markup-validator)
        - [**W3C Jigsaw CSS Validator**](#w3c-jigsaw-css-validator)
        - [**PEP8 Validator**](#pep8-validator)
    - [**Browers Testing**](#browers-testing)
    - [**User Stories Testing**](#user-stories-testing)
        - [**User Story 1**](#user-story-1)
        - [**User Story 2**](#user-story-3)
        - [**User Story 3**](#user-story-3)
    - [**Manual testing**](#manual-testing)
        - [**Home**](#home)
        - [**Drinks**](#drinks)
        - [**Booking**](#booking)
        - [**Cart**](#cart)
        - [**Checkout**](#checkout)
    - [**Known Issues**](#known-issues)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment on Heroku**](#remote-deployment-on-heroku)
6. [**Credits**](#credits)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)
    - [**Disclaimer**](#isclaimer)

---

## UX

### Design Objectives
#### Deign a Application Appropriate for Audience
#### Content Relevance and Accuracy
#### Content Grouping
#### Technology 

### User stories

### Design
#### Framework
#### Colors
#### Icons
- [Font Awesome](https://fontawesome.com/)
    - The Font Awesome icons where used as they provide a wide array of attractive and useful icons and I found these to be sufficient for my project.
#### Typography

### Wireframe
#### Desktop Wireframes
#### Mobile Wireframes


## Features


### Existing Features

#### All Pages
#### Home
#### Drinks
#### Booking
#### Cart
#### Checkout
#### Search
#### Login
#### Registration

### Features Left to Implement


## Technologies Used

### Frontend Technologies
### Back-End Technologies
**Python**
    - [Python 3.7.6](https://www.python.org/) - Used as the programming language at the back-end.
**Django**
**Heroku**
    - [Heroku](https://www.heroku.com) - Used for hosting the deployed website.


## Testing


### Code Validators
#### WC3 Markup Validator
#### W3C Jigsaw CSS Validator
#### PEP8 Validator


### Browers Testing
This website was tested on multiple browsers. They included:
- [Google Chrome](https://www.google.com/chrome/)
- [Microsoft Edge](https://www.microsoft.com/en-us/edge)
- [Firefox](https://www.mozilla.org/en-US/firefox/new/)


### User Stories Testing

### Manual Testing
#### Home
#### Drinks
#### Booking
#### Cart
#### Checkout
#### Login
#### Registration
#### Known Issues


## Deployment


### Local Deployment
To run this project locally on any system the following will need to be installed

- [Python3](https://www.python.org/downloads/) to run the app.py files and the application
- [PIP](https://pip.pypa.io/en/stable/)
- An IDE such as [Gitpod](https://gitpod.io/) or [Microsoft Visual Studio](https://code.visualstudio.com/)
- [GIT](https://www.atlassian.com/git/tutorials/install-git)

To clone or copy this project from GitHub follow these steps:
1. Follow this link to the [project repository on GitHub] (https://github.com/DarrenCoppinger/milestone-project-4.git)
2. On the left side of the page click the green button labelled "Clone or Download"
3. In the pop up that appears labelled "Clone with HTTPs" section copy the URL
4. In your local IDE open Git Bash
5. Change the working directory to the location for the cloned directory to be stored.
6. Type "git clone" into the GIT CLI terminal and then paste in the URL copied from GitHub in step 3 (i.e. git clone https://github.com/DarrenCoppinger/milestone-project-4.git )
7. Hit enter and create your local drive.
8. Install the necessary requirements from the requirements.txt file using the command `pip3 install -r requirements.txt`
9. Generated a env.py file where you will store your environmental variables:
    - SERCRET_KEY
    - STRIPE_PUBLISHABLE
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
10. Set the SERCRET_KEY to your preferred value. 
11. Run the application by typing the following command into the CLI:
    - python3 manage.py runserver



### Remote Deployment on Heroku
This app is currently deployed on heroku. The deployment is the code stored on the master branch of the project on GitHub. To deploy this project to Heroku required the following steps:
1. Register for Heroku and once signed in click the "New" button on the dashboard to create a new app.
2. In Heroku Name the app and specify the region (Europe in my case). 
3. Create a requirement.txt file to allow Heroku to install the required dependencies to run the app. The CLI text to input is as follows `pip3 freeze --local > requirements.txt`
4. Create a Procfile to inform Heroku what type of app is being deployed `echo web: python run.py > Procfile`
5. On the deployment tab of your project in Heroku click the Heroku GIT method for deployment.
6. In the CLI of you IDE input the following:
 ```
 $ heroku login
 $ heroku git:remote -a <BarTender>
 $ git push heroku master
 ```
7. In the resources panel of Heroku type Postgres into the Add-ons search bar and then click the Provision button to add this as a resource.
8. Set up AWS S3 Bucket and Stripe account
9. In the Heroku settings tab, click on the  "Real Config Vars" button to set environmental variables as follows:
 - AWS_ACCESS_KEY_ID: `<your_aws_key>`
 - AWS_SECRET_ACCESS_KEY: `<your_secret_aws_key>`
 - DATABASE_URL: `<postgres_database_link>`
 - DISABLE_COLLECTSTATIC: `1`
 - EMAIL_ADDRESS: `<your_email_address>`
 - EMAIL_PASSWORD: `<your_email_password>`
 - SERCET_KEY: `<your_secret_key>`
 - STRIPE_PUBLISHABLE: `<your_stripe_publishable_key>`
 - STRIPE_SECRET: `<your_stripe_secret_key>`
 
 10. In the top right of the heroku dashboard press the "Open App" button to view your deployed Heroku app.


## Credits
### Media
Images used in this site were sourced from the [Wikimedia Commons](https://commons.wikimedia.org/).

### Acknowledgements
- [Antonio Rodriguez](https://github.com/AkaAnto)
    - My Code Institute mentor.

### Disclaimer
This Website was produced for educational purposes only.