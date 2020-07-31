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
- search the website for a drink

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
Wireframes for both the desktop and mobile versions of the website were produced. They are include below:
#### Desktop Wireframes
- [Home](https://i.ibb.co/d6VGZBh/Home.png)
- [Booking](https://i.ibb.co/VBT3YP4/Booking.png)
- [Drinks](https://i.ibb.co/F6Gqzm1/Drinks.png)
- [Drink Description](https://i.ibb.co/DbQG6Y0/Product-Page.png)
- [Cart](https://i.ibb.co/cxgKzfp/Cart.png)
- [Checkout](https://i.ibb.co/fSLy6Zq/Checkout.png)
- [Login](https://i.ibb.co/BVKrFnG/Login.png)
- [Registration](https://i.ibb.co/wcLsW36/Register.png)

#### Mobile Wireframes
- [Home](https://i.ibb.co/p4mZw8K/Home-mobile.png)
- [Booking](https://i.ibb.co/Rzc3w1v/Booking-mobile.png)
- [Drinks](https://i.ibb.co/R2PDQHV/Drinks-mobile.png)
- [Drink Description](https://i.ibb.co/BZns43m/Products-mobile.png)
- [Cart](https://i.ibb.co/F0CyDXk/Cart-mobile.png)
- [Checkout](https://i.ibb.co/0ZZDm56/Checkout-mobile.png)
- [Login](https://i.ibb.co/Rp0jBXd/Login-mobile.png)
- [Registration](https://i.ibb.co/G2pqtZp/Register-mobile.png)

## Features
Major features to be developed and deployed on this website are summarized in the following table and graph. In the below opportunites analysis, the viability/feasibility is lower than the importance total. Therefore, all the features on this list will not be implemented. The Booked out feature was left for a later development sprint.

| Opportunities | Importance | Viability/feasibility | Difficulty |
|:---|:---:|:---:|:---:|
|Booking functionality to receive and store requests|5|4|5|
|Automatic emails on booking request and on processing request from backend|5|3|5|
|Menu/drinks page with sort functionality (by item category)|4|4|4|
|Backend feature to add new products/drinks|4|5|3|
|User Registration and Login|4|5|3|
|Cart and Checkout feature with the ability to take payments|4|3|4|
|Contact page for general user communications|3|4|3|
|Interactive map showing business location|3|4|3|
|Booking app add time slots and remove seat options when unavailable (Booked Out feature)|3|3|5|
| **Total** | **33** | **32** |  | 

![Viability Feasability Study](https://i.ibb.co/SxQ0wFG/Viability-Feasability-Study.jpg)

### Existing Features
#### All Pages
All pages include a responsive navigation bar and title at the top of the page. The title and logo act as a "Home" button. On medium and small screen size the navbar reduces to just the title and logo, with the page's buttons concealed in a sidebar accessible via a menu icon in the left-hand corner of the navbar. 

The navbar contains the Home, Booking, Drinks, Cart and a Login button. If the user is logged into an account the login button will change to a "Logout" button.

Each page has a message panel that appears when a messages is generated. 

#### Home
The Home page includes background image of a cocktail bar with is fixed in position at the center of the page. A floating transparent container appears infront of the image which has a greeting statement. There are also two link buttons in the contain which change depending on whether the user is logged in or not. If they are not logged on the buttons will direct the user to the "Login" and "About" page. If the user is logged in the buttons will direct them to the "Booking" and "Drinks" pages.

#### Drinks
The drinks page presents the drinks added to the database. By default the page is loaded with the all the entries loaded. 

At the top of the page is a arrangement of buttons which have the names of the catagories defined in the database "Pints", "Bottles", "Soft Drinks", "Cocktails" and "Spirits". The "All" button is the default view which displays all catagories. Each of the other buttons will limit the entries presented to a single catagory.

Each entry on the Drinks page is represented as a Bootstrap Card. Each card has an image, title, decription and price associated with it. Underneath these details is a small form which allows the user to select the number of the item they wish to add to their Cart and then click the "Add" button to execute this. 

Each card has a hoover effect to indicate that if clicked it will provide more information by bringing the user to the drinks individual page. THis is also indicated by the truncated presentation of the description text underneath it's image.

The page is designed to be responsive and will the number of entries in a row will vary depending on the screen width as follows:
- 992px < width : 4 entries per row
- 768px < width < 992px : 3 entries per row
- 576px < width < 768px  : 2 entries per row
- width < 576px : 1 entry per row

#### Booking
The Booking page presents users with the ability to request a particular type of seat in the bar for a particular time. 

The Booking page includes input fields for all the required information to make a reservation, these include: Seat Type, Full Name, Phone Number, Date, Booking Start Time and Booking End Time. Widgets were used for the date and time fields. This ensures that the user can only use the date or time picker (the calendar and clock icons) to fill in these fields. This reduces the chances of incorrect or unclear data being submitted in the form.

This feature requires the user to add in additional details that the did not provide during their registration (Full Name and phone number). During the design of the website it was considered adding these details into the registeration process. However, it was considered an simpler solution to only ask the user information when it was absolutely necessary.

A "Floor Plan" of the bar is also included on the right hand side of the page. This column will move to underneath the "Booking Details" form on screens of less than  768px (the md breakpoint).

#### Cart
The Cart page presents a summary of all the items add to the users cart. If the user has not added an item to their cart they will be show the message "YOUR CART IS EMPTY".

When the user adds a itme to the cart from the Drinks page they will receive the message "Item successfully added to your Cart!" and a badge with a number will appear beside the Cart icon in the Navbar.

Each item in the Cart has a image, title, price and quantity. The quantity can be adjusted to using an input field. It the field is set to 0 and the "AMEND" button clicked the item will be removed from the Cart. 

At the bottom of the page there is "Total" section which shows the user the total cost of all the items in their Cart.


#### Checkout
#### Search
#### Login
#### Registration

### Features Left to Implement
Booked Out Feature
Pagination on the Drinks Page

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