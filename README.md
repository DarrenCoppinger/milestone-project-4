[![Build Status](https://travis-ci.org/DarrenCoppinger/milestone-project-4.svg?branch=master)](https://travis-ci.org/DarrenCoppinger/milestone-project-4)

# BarTender - Milestone 4 Project

![BarTender Project Image](https://i.ibb.co/s6J6dMv/bartender-banner.jpg)

## [Deployed BarTender website here](https://bartender-ms4.herokuapp.com/)

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
This website was designed as a part of my Code Institute Full Stack Development course, specifically the Full Stack Framewords with Django module.

The website provides users with a tool that allows them to book a seat in a bar on the "Booking" page. Through the admin functionality of the website the the bar staff can approve, deny or amend the booking request (potentially after contacting the customer directly). 

The website also provides the customer with a list of the products available in the bar on the "Drinks".
### Design Objectives
The following are the main design objectives for the project:

#### Design a Application Appropriate for Audience
The website must be appropriate for the audience. The audience for this website will be English speaking, technology savvy and will likely access the site on mobile devices. Although the website will accommodate all visitors, its primary audience will be technology literate. Using the bootstrap framework means that this website has a mobile first approach to development however, it will also perform well on a large screen sizes.
#### Content Relevance and Accuracy
The content to the site must be relevant to the site owners and their audience. As such, products on sale through the website can be add through the backend of the site. Products can be edited and updated as required.

#### Content Grouping

The website content is grouped into easily understood sections (Home, Booking, Drinks, Login/Logout, Cart).
#### Technology 

Appropriate technologies were used to design the website such as [Bootstrap](https://getbootstrap.com/), [Django](https://www.djangoproject.com/), [EmailJS](https://www.emailjs.com/), [Google Maps JavaScript API](https://developers.google.com/maps/documentation/javascript/tutorial)  to provide the user with a high-quality experience. 

To manage the data two different relational (SQL) databases were used. For local deployment and development of the site Django's default database, SQLite3, was used. For the deployed site [Heroku Postgres](https://www.heroku.com/postgres) database was used.

### User stories
A user who visits the website might follow one of these forms:
- A user wants to book a particular type of seat for a certain date and time in the bar.
- A user wants to look through the drinks/products that are available on from the bar.
- A user wants to order drinks to a table that they are sitting at through a completely contactless means.

Additionally, the following requirements should be met by the website:

"As a user of this website, I would like to- _____________________"
- view the website from all device types (mobile, tablet or desktop)
- contact the site adminstrators to make a inquiry



### Design
The style of the site is inspired by the aesthetic of classic cocktail club. These clubs tend to have dark, cool and simple design.

#### Framework
For this project the framework [Django](https://www.djangoproject.com/) was used.

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
- [HTML](https://www.w3schools.com/html/html5_intro.asp) - Employed for markup text. 
- [CSS](https://www.w3schools.com/css/) - Used for cascading styles.
- [jQuery 3.4.1](https://code.jquery.com/jquery/) - Used for JavaScript functionality.
- [Bootstrap 4.5.0](https://getbootstrap.com/) - Used for the design framework.
### Back-End Technologies
**Python**
 - [Python 3.7.6](https://www.python.org/) - Used as the programming language at the back-end.
**Django**
- [Django](https://www.djangoproject.com/)
**Heroku**
    - [Heroku](https://www.heroku.com) - Used for hosting the deployed website.


## Testing
The follow validators were used to check the code developed from this project:
- [WC3 Markup Validator](https://validator.w3.org/)
- [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/)

### Code Validators
#### WC3 Markup Validator
 [WC3 Markup Validator](https://validator.w3.org/) was used to validate the HTML code. However, the validator is not able to recognise the Jinja templating syntax so some errors were recorded. All code other than the template syntax language was successfully validated.
#### W3C Jigsaw CSS Validator
[W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS code. The CSS successfully passed this check with no errors.
#### PEP8 Validator
[PEP8 Validator](http://pep8online.com/) was used ti validate my python code.

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