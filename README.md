[![Build Status](https://travis-ci.org/DarrenCoppinger/milestone-project-4.svg?branch=master)](https://travis-ci.org/DarrenCoppinger/milestone-project-4)

# BarTender - Milestone 4 Project

![BarTender Project Image](https://i.ibb.co/s6J6dMv/bartender-banner.jpg)

## [Deployed BarTender website here](https://bartender-ms4.herokuapp.com/)

---

## Introduction
This website, [BarTender](https://bartender-ms4.herokuapp.com/), was designed as a part of my Code Institute Full Stack Development course, specifically the Full Stack Frameworks with Django module.
The website is an online tool for a fictitious bar of the same name. 

## Table of Contents
0. [**Introduction**](#introduction)
1. [**UX**](#ux)
    - [**Aims**](#aims)
        - [**User Aims**](#user-aims)
        - [**Business Aims**](#business-aims)
    - [**Design Objectives**](#design-objectives)
        - [**Appropriate for Audience**](#appropriate-for-audience)
        - [**Content Relevance and Accuracy**](#content-relevence-and-accuracy)
        - [**Content Grouping**](#content-grouping)
        - [**Technology**](#technology)
    - [**User stories**](#user-stories)
    - [**Design**](#design)
        - [**Frameworks**](#frameworks)
        - [**Colours**](#colours)
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
        - [**Contact**](#contact)
    - [**Features Left to Implement**](#features-left-to-implement)
3. [**Technologies Used**](#technologies-used)
    - [**Frontend Technologies**](#frontend-technologies)
    - [**Backend Technologies**](#Backend-technologies)
4. [**Testing**](#testing)
    - [**Code Validators**](#code-validators)
        - [**WC3 Markup Validator**](#w3c-markup-validator)
        - [**W3C Jigsaw CSS Validator**](#w3c-jigsaw-css-validator)
        - [**PEP8 Validator**](#pep8-validator)
    - [**Browser Testing**](#browers-testing)
    - [**User Stories Testing**](#user-stories-testing)
        - [**User Story 1**](#user-story-1)
        - [**User Story 2**](#user-story-3)
        - [**User Story 3**](#user-story-3)
    - [**Manual testing**](#manual-testing)
        - [**Test Navbar and Footer**](#test-navbar-and-footer)
        - [**Test Home**](#test-home)
        - [**Test Booking**](#test-booking)
        - [**Test Drinks/Listings Pages**](#test-drinks/listings-pages)
        - [**Test Cart**](#test-cart)
        - [**Test Checkout**](#test-checkout)
        - [**Test Contact**](#test-contact)
        - [**Test About**](#test-about)
    - [**Known Issues**](#known-issues)
    - [**Automated Testing**](#automated-testing)
        - [**Python Testing**](#python-testing)
        - [**Coverage**](#coverage)
        - [**Travis**](#travis)
5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment on Heroku**](#remote-deployment-on-heroku)
6. [**Credits**](#credits)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)
    - [**Disclaimer**](#isclaimer)

---

## UX
This website has a number of user and business aims. They are as follows:

### Aims
#### User Aims
The user aims for this website are to:
- provide a booking system for customers to request a type of seat in the bar for a particular date and time
- provide a drinks/products page to act as a complete menu of what is available to the customer (this removes the requirement of a physical menu)
- provide a completely contactless way for customers to construct and place an order from the bar for a particular table.
- provide a contactless way for a customer to pay for an order they have constructed

#### Business Aims
The business aims for this website are to:
- provide a database of booking requests from customers for staff to review.
- reduce staff workload creating a booking system that sends automatic emails to the customers when the status of their application changes.
- provide a contactless payment mechanism to remove the requirement of processing payments through a card machines or cash.
- provide a mechanism for customers to make enquires through the website.

### Design Objectives
The following are the main design objectives for the project:
- The website must be appropriate for the audience. 
- The content to the site must be relevant to the audience and site owners.
- The website content must be grouped into easily understood sections.

#### Appropriate for Audience
The audience for this website will be English speaking, technology savvy and will likely access the site on mobile devices. 

Although the website will accommodate all visitors, its primary audience will be technology literate. Using the bootstrap framework means that this website has a mobile first approach to development. However, it will also perform well on larger screen sizes.

#### Content Relevence and Accuracy
The content to the site must be relevant to the site owners and their audience. 

As such, the website operator/administrator can add products to the Drinks page through the backend of the site. Products can be edited and updated as required. This ensures that the content of the website is relevant.

#### Content Grouping
The website content is grouped into easily understood sections (Home, Booking, Drinks, Login/Logout, Register, Cart, Checkout, About Us, Contact Us). 

Logged out users are also only able to access the Home, Register, Login/Logout, About Us and Contact Us. Only logged in users can access the Booking, Drinks, Cart and Checkout pages.

#### Technology 
Appropriate technologies were used to design the website such as [Bootstrap](https://getbootstrap.com/), [Django](https://www.djangoproject.com/), [EmailJS](https://www.emailjs.com/), [Google Maps JavaScript API](https://developers.google.com/maps/documentation/javascript/tutorial) to provide the user with a high-quality experience. 

To manage the data two different relational (SQL) databases were used. For local deployment and development of the site Django's default database, SQLite3, was used. For the deployed site [Heroku Postgres](https://www.heroku.com/postgres) database was used.

### User stories
A user who visits the website might follow one of these forms:
- A user wants to book a particular type of seat for a certain date and time in the bar.
- A user wants to look through the drinks/products that are available on from the bar.
- A user wants to order drinks to a table that they are sitting at through a completely contactless means.

Additionally, the following requirements should be met by the website:

"As a user of this website, I would like to- _____________________"
- view the website from all device types (mobile, tablet or desktop)
- contact the site administrators to make an inquiry
- search the website for a drink

### Design
The style of the site is inspired by the minimalist aesthetic of a modern cocktail club. These clubs tend to have dark, cool and simple designs.

To achieve this the [Bootswatch](https://bootswatch.com/) theme [Lux](https://bootswatch.com/lux/) was used and amended as required to fix the projects requirements.

#### Frameworks
For this project the framework [Django](https://www.djangoproject.com/) was used. Additionally, [Bootstrap](https://getbootstrap.com/) was used for the design framework.

#### Colours
The main colours used, which are primary form the Lux bootswatch style, are as follows:
- ![#1a1a1a](https://placehold.it/15/1a1a1a/1a1a1a) `#1a1a1a` (**off black**)
- ![#f7f7f9](https://placehold.it/15/f7f7f9/f7f7f9) `#f7f7f9` (**light grey**)
- ![#800000](https://placehold.it/15/800000/800000) `#800000` (**maroon**)
- ![#d9534f](https://placehold.it/15/d9534f/d9534f) `#d9534f` (**coral red**)

#### Icons
- [Font Awesome](https://fontawesome.com/)
    - The Font Awesome icons where used as they provide a wide array of attractive and useful icons and I found these to be sufficient for my project.

#### Typography
The font used for this project is [Nunito Sans](https://fonts.google.com/specimen/Nunito+Sans). It is included through the use of the Bootswatch theme [Lux](https://bootswatch.com/lux/).

This suited the simple minimalist clean aesthetic that the author had in mind for the website and so was not changed.

### Wireframe
Wireframes for both the desktop and mobile versions of the website were produced. They are included below:

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
### Opportunities Analysis
At the beginning of this project the major features to be developed and deployed on this website planned. The results of this preliminary analysis are summarized in the following table and graph. 

In the below opportunities analysis, the viability/feasibility is lower than the importance total. Therefore, all the features on this list will not be implemented. The "Booked Out feature" was left for a later development sprint.

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
|Booking App: add time slots and remove seat options when unavailable (Booked Out feature)|3|3|5|
| **Total** | **33** | **32** |  | 

![Viability Feasability Study](https://i.ibb.co/SxQ0wFG/Viability-Feasability-Study.jpg)

### Existing Features
#### All Pages
All pages include a responsive navigation bar (navbar) and title at the top of the page. The title and logo act as a "Home" button. On medium and small screen sizes the navbar reduces to just the title and logo, with the page's buttons concealed in a sidebar accessible via a menu icon in the left-hand corner of the navbar. 

If the user is logged in the navbar contains the Home, Booking, Drinks, Cart and a Logout buttons. If the user is logged out only the Home, Register and Login buttons will be displayed.

Each page has a message panel that appears directly under the navbar when a message is generated. 

#### Home
The Home page includes background image of a cocktail bar which is fixed in position at the centre of the page. A floating transparent container appears in front of the image which holds a greeting statement. There are also two buttons at the bottom of the container which change depending on whether the user is logged in or not. If they are not logged on the buttons will direct the user to the "Login" and "About" pages. If the user is logged in the buttons will direct them to the "Booking" and "Drinks" pages.

#### Booking
The Booking page allows users to request a particular type of seat in the bar for a particular time. 

The Booking page includes input fields for all the required information to make a reservation. These fields are defined in the Reservation model and are as follows: 
- Seat Type
- Full Name
- Phone Number
- Date
- Booking Start Time
- Booking End Time

A final model field is excluded from the customers booking form (ReservationForm), that is the "Status" field. This is used by the staff to define whether the booking has been accepted or not. The field has three set options: "Requested", "Accepted" or "Denied". By default, it is set to "Requested" until altered by a member of staff.

Widgets were used for the date and time fields so they must be input in date and time format. On the MS Edge and Google Chrome browsers the user can use the date or time picker instruments (by clicking the calendar or clock icons) to fill in these fields. These measures reduce the chances of incorrect data being submitted in the form.

The Booking feature also requires the user to add in additional details that were not provided during registration (Full Name and phone number). During the design of the website the author considered adding these details into the registration form so they could be passed into the Booking form as initial data. However, it was decided that is was a simpler solution to only ask the user for this information only when it was necessary.

A "Floor Plan" of the bar is also included on the right side of the page to provide the user with an overview of the bar's layout. This column will move to underneath the "Booking Details" form on screens of <768px.

A member of BarTender's staff who is set up as a superuser/administrator of the website will be able to access all the requested booking applications from the Bookings panel in the Admin section of the website. The staff member can review and change any details of the booking from the admin panel. If there is an issue with seat availability at a certain time, they have the contact details of the customer in the booking form so they can be contacted to discuss any changes. 

If the booking is altered and saved the customer will receive an updated automatic email with these details. If the booking is accepted the staff member can change its status from "Requested" to "Accepted" this will result in a different automatic email being sent to the customer. Similarly, if the status is changed to "Denied" another automatic email is sent to the customer.

These emails can be found at the following location in the project files:
-  Booking Requested email: [request.txt](booking/templates/mail/accepted.txt)
-  Booking Accepted email: [accepted.txt](booking/templates/mail/accepted.txt)
-  Booking Denied email: [denied.txt](booking/templates/mail/accepted.txt)

#### Drinks
The Drinks page presents the drinks/products added to the Product model. By default, the page is loaded with the all the entries displayed. 

At the top of the page is an arrangement of buttons which have the names of the categories defined in the database "Pints", "Bottles", "Soft Drinks", "Cocktails" and "Spirits". The "All" button is the default view which displays all categories. Each of the other buttons will limit the entries presented to a single category.

Each entry on the Drinks page is represented as a Bootstrap Card. Each card has an image, title, description (truncated to 30 characters) and price associated with it. Underneath these details is a small form which allows the user to select the number of the item they wish to add to their Cart and then click the "Add" button to execute this. 

Each card has a hoover effect to indicate that if clicked it will provide more information by bring clicked. It does this by bringing the user to the drinks individual listing page (listing.html). This is also indicated by the truncated presentation of the description text underneath the items image.

The page is designed to be responsive and with the number of entries in a row varying depending on the screen width as follows:
- 992px < width : 4 entries per row
- 768px < width < 992px : 3 entries per row
- 576px < width < 768px  : 2 entries per row
- width < 576px : 1 entry per row

A superuser/administrator of the site can use the Products section of the websites admin panel to add additional drinks/products to the Products database. The superuser simply needs to click the "Add Product" button and populate the following model fields:
- Category (choice of Pints, Bottles, Soft-drinks, Cocktails or Spirits)
- Name
- Description
- Price
- Image (although not mandatory, for aesthetic purposes, product images should have a 1:1 aspect ratio)

#### Cart
The Cart page presents a summary of all the items added to the user's cart. If the user has not added an item to their cart, they will be shown the message "YOUR CART IS EMPTY".

When the user adds an item to the cart from the Drinks page they will receive the following message displayed under the navbar "Item successfully added to your Cart!". A badge with a number will also  appear beside the Cart icon in the Navbar.

Each item in the Cart has an image, title, price and quantity. The quantity can be adjusted by using an input field. If the field is set to 0 and the "AMEND" button clicked the item will be removed from the Cart. 

At the bottom of the page there is "Total" section which shows the total cost of the items currently in the Cart.


#### Checkout
The checkout page presents an Order Summary and a Payment Details form. The Order Summary presents an image, title, price and quantity of each item added to the cart. Underneath this is also presents a "Total" for the cost of the items in the Cart.

The checkout page also displays the Payment Details form which is made up of two forms, the Order Form and the Payment Form. The Order Form requires the user to input their table number, Full Name and phone number.

Underneath the Order Form is the Payment Form. This requires the credit card details of the user (Credit card number, CVC Expiry Month and Expiry Year). Any Errors generated through submission of this form will appear above the form. Error messages are coloured red and underlined.

Underneath these forms is a "Confirm Order" button to submit the payment details. There is also "Go to Cart" button to bring the user back to their cart view to make any alterations they require.

Orders submitted by customers can be reviewed and acted on by site administrators in the Checkout section of the admin site.

#### Search
A search bar is built into the NavBar in the base.html template and so is present on every page. If the user is not logged in, executing a search in the search bar will redirect them to the login page.

If a search is executed when the user is logged in, the user is directed to the results on the  Drinks page (product.html). The search query will look for results in the Products model database.

#### Registration

The registration page has four fields: Email, Username, Password, Password Confirmation. All fields are required for form submission to be successful.

Error messages are generated on this page in the following scenarios:
- If the user enters an Email that has been used to create an account previously, they will receive the error message "Email address must be unique".
- If the user enters a Username that has been used to create an account previously, they will receive the error message "A user with that username already exists".
- If the user enter data in both Password and Password Confirmation fields but the values are not the same, they will receive the error message "Passwords must match".

If the user enters all fields and the form is successfully validated, they will be redirected to the home page and receive a message under the navbar of "You have successfully logged in!".

#### Login
The login page is accessed via a button on the navbar or the sidenav on mobile devices. Clicking this brings the user to the user login form page. The page has two fields, "Username" and "Password" with a submit button labelled "Login". 

- If the user has not registered for an account but tries to login by inputting an unregistered username and password they will see a message under the navbar saying "Your username or password is incorrect. Note that both fields may be case-sensitive."
- If the user enters both an existing username and a correct password, they will be redirected to the home page of the site and shown a message of "You have successfully logged in!"

If the user has signed up to the site but forgotten their password, they can click the "Reset Password" button underneath the login form. This will bring them to a "Password Reset" which will require them to input the email address they used during registration. Submitting, this form will send an email to this address allowing the user to reset their password.

All page templates used in this process are bespoke and styled in the same manner as the reset of the website.

#### Contact 
The contact page provides a place for customers to get in touch with the BarTender staff. All fields of the form (Username, email address and Message) must be populated for the form to be submitted.

On submission of the contact form the user will receive a copy of their message to the email address that was entered in the form. 

### Features Left to Implement
There are a number of features which were developed during the building of this website that could not be included in the final version. They will be address in a future development sprint. 

These features include:
- In the booking model: creating discrete time slots for each available seat in the bar. This would allow unavailable time slots to be highlight by the form so the customer would know the needed to choose another option (Booked Out Feature).
- Add Pagination on the Drinks Page (import if number of drinks/products grows larger)
- Generate automatic emails to the customer when an Order and Payment Form are submitted to confirm their order and act as a receipt.
- Add a profile page to display the user information and provide a way for these details to be updated.
- Develop Ajax supported form submissions on the Drinks page to stop the page reloading after an item is add to the cart.
- Link all orders for a particular table to a specific booking. This would allow the passing of the customers details from the Reservation Form to the Order Form and reduce the need for the customer to enter in this information twice. 

## Technologies Used
### General Technologies
- [Gitpod](https://gitpod.io/) - IDE used for development
- [GitHub](https://github.com/) - Used as remote storage for project
- [balsamiq](https://balsamiq.com/) - Used for wireframes


### Frontend Technologies
- [HTML](https://www.w3schools.com/html/html5_intro.asp) - Employed for markup text. 
- [CSS](https://www.w3schools.com/css/) - Used for cascading styles.
- [jQuery 3.4.1](https://code.jquery.com/jquery/) - Used for JavaScript functionality.
- [Bootstrap 4.5.0](https://getbootstrap.com/) - Used for the design framework.
- [Stripe](https://stripe.com/) - Used to make secure payments

### Back-End Technologies
- [Python 3.7.6](https://www.python.org/) - Used as the programming language at the back-end.
- [Django 1.11.29](https://www.djangoproject.com/)
- [Heroku](https://www.heroku.com) - Used for hosting the deployed website.
- [PostgreSQL ](https://www.heroku.com/postgres) - A relational SQL database used as plugin through Heroku.
- [AWS](https://aws.amazon.com/) - S3-Bucket and IAM used to host static and media files.
- [EmailJS](https://www.emailjs.com/) - Used to manage contact form

Details of all the packages used in this project can be found in the [requirements.txt](requirements.txt) file.

## Testing
Both automated and manual testing was used in the development of this site. Additonally, online validators were used to validate the code written for this project. Finally, the project was test on a number of browser to assess it's compatibility with them.

### Code Validators
The follow validators were used to check the code developed from this project:
- HTML - [WC3 Markup Validator](https://validator.w3.org/)
- CSS - [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/)
- JavaScript - [JShint Validator](https://jshint.com/)
- Python - [PEP8 Validator](http://pep8online.com/) 

#### WC3 Markup Validator
[WC3 Markup Validator](https://validator.w3.org/) was used to validate the HTML code. 

All errors highlight by the validator were dealt with apart from those caused by the templating language (i.e. statements inside "{%%}" of "{{}}") which were caught by the validator but are not errors.

Examples of these errors are:
- `Non-space characters found without seeing a doctype first. Expected <!DOCTYPE html>`
- `Consider adding a lang attribute to the html start tag to declare the language of this document`

These are present in templates that extend the base.html template. Again, this is not an error but a result of the validator not recognising the templating language. 

Additionally, there is another common templating error generated by using templating language to define a href or src value. This error has the form:
- `Bad value {% url 'example' %} for attribute href on element a: Illegal character in path segment: "{" is not allowed.`

Again, this is not an error but a result of the validator not recognising the templating language. 

#### W3C Jigsaw CSS Validator
[W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS code. The CSS successfully passed this check with no errors.

#### JShint Validator
[JShint Validator](https://jshint.com/) was used to validate my JavaScript code. The follow feedback provided by the validators. However, each of the errors can be explained and so do not need to be acted on.
- maps.js
    - Metrics: 
        -There is only one function in this file. It takes no arguments. This function contains only one statement. Cyclomatic complexity number for this function is 1.
    - One undefined variable:
        - google (Used by Google Maps JS API)
    - Two unused variables:
    	- markers (Used by GoogleMaps JS API)
        - initMap (Used by Google Maps JS API)
- sendEmail.js
    - Metrics: There are 3 functions in this file. Function with the largest signature take 1 arguments, while the median is 1. Largest function has 2 statements in it, while the median is 2. The most complex function has a cyclomatic complexity value of 1 while the median is 1.
    - One undefined variable:
        - emailjs (used by the EMAILJS API)
    - One unused variable
        - sendMail (called on contact.html page by submitting form)
- stripe.js
    - Metrics: 
        - There are 3 functions in this file. Function with the largest signature take 2 arguments, while the median is 0. Largest function has 11 statements in it, while the median is 4. The most complex function has a cyclomatic complexity value of 2 while the median is 1. 
    - Two undefined variables: 
    	- $ (used for jQuery)
        - Stripe (used for Stripe API)

#### PEP8 Validator
[PEP8 Validator](http://pep8online.com/) was used to validate my python code. However, there were two remaining errors left in the settings.py file which are as follows:
- 'env' imported but not used
    - this is incorrect as the env variables are import and used in the local deployment of this project
- line 107 too long (83 > 79 characters)
    - this is a line from the original Django code and is as follows: 
    `'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'`
    - As the line is the specifying a validator it was not altered.

### Browser Testing
This website was tested on multiple browsers. They included:
- [Google Chrome](https://www.google.com/chrome/)
- [Microsoft Edge](https://www.microsoft.com/en-us/edge)
- [Firefox](https://www.mozilla.org/en-US/firefox/new/)

### User Stories Testing

#### User Story 1
**A user wants to book a particular type of seat for a certain date and time in the bar.**
1. The user loads the site and is directed to the index.html page. The user sees the instructions on the page and the click the register button.
2. The user submits a completed registration form is redirected to the home page where there is a success message of "You have successfully registered" underneath the navbar.
3. On the home page the user sees the buttons have now changed to "Booking" and "Drinks". Additionally, the navbar has changed from "Home", "Register" and "Login" to "Home", "Booking", "Drinks", "Logout" and "Cart". The user clicks the "Booking" button on either the page or the navbar.
4. The user sees the floor plan on the left of the "Booking" page showing the layout of the bar.
5. The user fills out the form choosing a Seat Type option (Bar Stool, Window Seat, Booth or Table), Phone number, date, Booking Start Time and Booking End Time. These field can generate the following types of validation errors:
    - If the user doesn't enter a valid phone number, they get the message "Enter a valid phone number (e.g. +353861234567)"
    - If the user chooses a date that has already past, they get the message "Invalid date - selected date passed"
    - If the user chooses a start or end time for the booking outside of the bars opening hours they get the error message "Booking must start/end during bar opening hours 12:30 - 00:00."
    - If the user chooses an end time that is earlier than the selected start time the error message "Booking can not end before it starts" will be displayed.
    - Each of the above errors generates a message under the navbar of "We were unable to make this reservation"
6. On submission of the booking form the user is redirected back to the home page with the message "You have requested a booking. A member of our staff will be in touch shortly to confirm your booking." underneath the navbar.
7. The user will also receive an automatic email (to the email provided during registration) specifying the "Booking Status", "Date", "Start Time", and "End Time". The email says that it will be followed up on by a member of staff. 
8. In a real world situation the user would be rang by the staff/site admin of BarTender to confirm their details and make any amendments to their booking dependant on seat availability at certain times.
9. After staff have reviewed and confirmed the booking with the user, the staff can change the status of the booking to either "Accepted" or "Denied" based on their interaction with the user. When the admin saves the changes to the booking request on the backend of the site, the user will receive an email with the confirmed details and the message "We are pleased to confirm your booking. We look forward to seeing you!".

#### User Story 2
**A user wants to look through the drinks/products that are available on from the bar to find a specific product.**
1. The User loads the site and is directed to the index.html page. The user see's the search bar in the top right corner of the screen. Into this they type in a search term and clicks search.
2. As the user isn't logged in, they are directed to the login page. As the user hasn't set up an account, they click the register button at the bottom of the page and are directed to the registration page.
3. The user submits a completed registration form and is redirected to the home page where there is a success message of "You have successfully logged in!" underneath the navbar.
4. On the home page the user sees the buttons on the have now changed to "Booking" and "Drinks". Additionally, the navbar has changed from "Home", "Register" and "Login" to "Home", "Booking", "Drinks", "Logout" and "Cart". The user clicks the "Drinks" button on either the page or the navbar.
5. The user is directed to the Drinks page (products.html) where all the current products available from the bar are displayed. 
6. The user sees that that there are buttons at the top of the Drinks page that describes the categories the drinks are broken down into (Pints, Bottles, Soft-drinks, Cocktails and Spirits).
7. The user can either search for the drink they are looking for by entering a search term in the search bar or by clicking the relevant category from the buttons at the top of the page. Either choice will generate a Drinks page with a subset of all the drinks in the Products database.
8. The user now can choose the exact product they are looking for. If the user clicks on the drinks/product entry they will be directed the products individual page (the products listing). This page will present the products image, name, full untruncated description and an input form for adding that item to their cart. If the user wishes to turn to the cart there is a redirect button at the bottom of the page which will bring them back to the Drinks page.

#### User Story 3
**A user wants to order a drink (specifically a cocktail) to their table and pay for it through contactless means.**
1. The user has already register for the site and logged in (as described in the first and second user stories presented above). They have booked a table in the bar and have taken their seats at the booking start time.
2. From the home page the user clicks the Drinks icon in the navbar and is directed to the Drinks page.
3. The user clicks the cocktail button at the top of the page to isolate the cocktails that are available.
4. The user reviews what is on the menu and chooses to order a drink. They navigate to the selected drink and use the form at the bottom of the entry to enter the number 4 (alternatively they could user the arrows on the right side of the input box to adjust the number being ordered). 
5. The user then clicks the add button and is redirected back to the full Drinks menu. The message "Item successfully added to your Cart!" is displayed under the navbar.
6. The user sees that a badge, with the number 4 inside it, has appeared beside the Cart icon in the navbar. The user clicks the cart icon and is directed to the cart page.
7. The user is presented with a summary of their order on the Cart page. The user realised they need to order another drink and so adjust the number in the quantity field to 5 and click the Amend Button beside it. This reloads the page and a success message of "Successfully adjusted item in your Cart!" is displayed under the Navbar.
8. The user is now satisfied that the order is correct and so clicks the "Checkout" button underneath the order total at the bottom of the page.
9. The user is directed to the checkout page. On the right side the user sees the final version of the order they have created with the total cost underneath it. On the right side they see a payment details form.
10. The user selects their table number (in a real world situation this would be specified on their table) and inputs their name and phone number (required in case there is difficulty locating the person who made the order).
11. The user inputs their credit card details (number, CVC, Expiry month, and expiry year). The user then clicks the "Confirm" button to submit the order. If user fills in the form incorrectly the following error can be displayed:
    - If the card number is entered incorrectly the error message "Your card number is incorrect." is displayed.
    - If the cards CVC is entered incorrectly the error message "Your card's security code is invalid." is displayed.
    - If the cards expiry month or year has passed the user will see error message "Your card's expiration month/year is invalid." displayed at the top of the form
    - If the user doesn't enter a valid phone number, they get the message "Enter a valid phone number (e.g. +353861234567)"
    - Each error above is also accompanied by an error message under the navbar of "We were unable to take payment with that card".
12. If the user successfully submits the Payment Details form, they are redirected to the Drinks page with the following success message displayed under the navbar "You have successfully paid".


### Manual Testing
#### Test Navbar and Footer
1. Navbar
    - Check that a logged out user sees the Home, Register and Login items in the navbar.
    - Check that a logged in user sees the Home, Booking, Drinks, Logout and Cart items in the navbar.
    - Visit a page of the website on a desktop sized screen (>992px).
    - Hover over the name text "BarTender" and logo to check that the hover effects work.
    - Click the navbar-brand text "BarTender" to check that it links to the Home page.
    - Hover over each navbar item to check the hover effect works for each one.
    - Click on each one of the navbar buttons to ensure that each links to the correct page.
    - Alter the screen size from desktop size down to medium devices (<992px) size to check that the navbar is responsive. At that size the navbar changes to the toggler icon with just the site name and logo. The menu items move to the sidenav menu.
    - Click the toggler icon to check that the drop-down sidenav menu activates.
    - Hover over each of the sidenav menu items and the login button to make sure their hover effect activates.
    - Click each of the drop-down menu buttons to make sure that they link to the correct page.

2. Footer
    - Check that the body element is always a minimum of 100% of the viewport height and that the footer is never floating in the middle of the screen
    - Check that the hover effects for the links in the Site Links section of the footer are reactive and that the Get Directions link hover effect is also reactive.
    - Check that the Google Maps API viewport is displaying and that the full screen view in its top right corner works.
    - Alter the screen size from above medium/tablet size down to small/mobile size (<768px) to check that the one row of four columns in the footer rearrange themselves into two rows of two columns.
    - Alter the screen size from small/mobile size down to extra-small/micro size (<576px) to check that the two rows of two columns in the footer rearrange themselves into four rows of one column.

3. Review of all functionality and responsiveness on mobile screen size by using [Responsinator](https://www.responsinator.com/).

#### Test Home
1. Logged Out
    - Check that the buttons in the central text area are "Register" and "About Us". Check that the buttons bring the user to the correct location.

2. Logged In
    - Check that the buttons in the central text area are "Booking" and "Drinks". Check that the buttons bring the user to the correct location.

3. Review of all functionality and responsiveness on mobile screen size by using [Responsinator](https://www.responsinator.com/).

#### Test Booking
- Visit the Booking page of the website on a desktop sized screen (>992px) to check that the page is displayed in 2 columns.
- Check that the page reduces to one column for <768px in width.
- Check that the floor plan image on the left side of the page, showing the layout of the bar, is loading correctly.
- Check that when the user fills out the form fields for Seat Type, Phone number, date, Booking Start Time and Booking End Time incorrectly the following types of validation errors are generated:
    - If the user doesn't enter a valid phone number, they get the message "Enter a valid phone number (e.g. +353861234567)"
    - If the user chooses a date that has already past, they get the message "Invalid date - selected date passed"
    - If the user chooses a start or end time for the booking outside of the bars opening hours they get the error message "Booking must start/end during bar opening hours 12:30 - 00:00."
    - If the user chooses an end time that is earlier than the selected start time the error message "Booking can not end before it starts" will be displayed.
    - Each of the above errors generates a message under the navbar of "We were unable to make this reservation"
- Check that on submission of the booking form the user is redirected back to the home page with the message "You have requested a booking. A member of our staff will be in touch shortly to confirm your booking." underneath the navbar.
- Check that the user receives an automatic email (to the email provided during registration) specifying the "Booking Status", "Date", "Start Time", and "End Time".
- Check that when an administrator (or staff member with access to the admin part of the website) make any amendments to the booking and saves the changes that the user receive another automatic email confirming this with the subject "Booking Request at BarTender - REQUEST ALTERED".
- Check that when an administrator of the site changes the status of the booking to either "Accepted" or "Denied" that the user receives an email with the confirmed details and the subject of either ""Booking Request at BarTender - ACCEPTED" or "Booking Request at BarTender - DENDIED".
- Review of all functionality and responsiveness on mobile screen size by using [Responsinator](https://www.responsinator.com/).

#### Test Drinks/Listings pages
- Visit the Drinks page of the website on a desktop sized screen (>992px) to check that the page is displays drinks entries (drinks display cards) in 4 columns to a row.
- Reduce the screen width to <992px to check the page changes to displays entries in 3 columns to a row.
- Reduce the screen width to <768px to check the page changes to displays entries in 2 columns to a row.
- Reduce the screen width to <576px to check the page changes to displays entries in 1 column to a row.
- Check that clicking each of the buttons at the top of the page limits the page entry to the categories they represent, i.e. Pints, Bottles, Soft-drinks, Cocktails, Spirits or All (all categories).
- Check that hovering over each drink entry triggers a box shadow effect.
- Check that the form at the bottom of each entries card is editable, that the value can be change both by typing and by using the arrows on the right of the input box.
- Check that clicking the "Add" button reloads the products page (products.html) with all database entries and the success message "Item successfully added to your Cart!".
- Check that when an item has been successfully added to the users cart a badge appears beside the cart icon in the navbar with the number of items in the cart shown.
- Check that when a product entry on the Drinks page is clicked, the products Listing page is launch and that the drinks name, image, untruncated description and price are displayed. A form should also be displayed underneath this allowing the user to select an amount and add that product to the user cart.
- Review of all functionality and responsiveness on mobile screen size by using [Responsinator](https://www.responsinator.com/).

#### Test Cart
- Visit the Cart page of the website and check that the page is responsive and that it displays drinks added to the cart in the following format:
    - Desktop width(>992px): the order item's image is displayed on the left side of the screen and on the right is shown the name, price, and input form allowing the user to adjust the amount of the product in the Cart.
    - Mobile width(>768px): the order item's image is displayed on top of the items name, price and input form allowing the user to adjust the amount of the product in the Cart
- Check that the total cost of the cart is correctly calculated and displayed at the bottom of the page
- Check that the input form at the bottom of the item entry loads the correct quantity of that item in the cart and that it can but adjusted by typing a different value or by using the arrows on the right of the input box.
- Check that if the quantity of an item is amended that the Cart page is reloaded with the success message "Successfully adjusted item in your Cart!"
- Check that when the Checkout button at the bottom of the Cart page is pressed that it loads the Checkout page.
- Review of all functionality and responsiveness on mobile screen size by using [Responsinator](https://www.responsinator.com/).

#### Test Checkout
- Visit the Checkout page of the website and check the page is responsive and that it displays the users Cart in the following format:
    - Desktop width(>992px): the order summary is shown on the left of the screen, this includes, on the left, each item's image and , to the right, the item's name, price and quantity of the item displayed. The payment details form is displayed on the right side of the screen.
    - Mobile width(>768px): the order summary is shown on the top of the page with each order item's image (on top) and the item's name, price and quantity displayed underneath. The Payment Details form is displayed under the Order Summary. 
- Check Confirm order button submits the Payment Details form (Order Form and Payment Form)
- Check that "Go to Cart" button brings the user back to the Cart page
- Check that if the user inputs their credit card number, CVC, Expiry month, or expiry year incorrectly and clicks the "Confirm Order" button the following errors can be displayed:
    - If the card number is entered incorrectly the error message "Your card number is incorrect." is displayed.
    - If the cards CVC is entered incorrectly the error message "Your card's security code is invalid." is displayed.
    - If the cards expiry month or year has passed the user will see error message "Your card's expiration month/year is invalid." displayed at the top of the form
    - If the user doesn't enter a valid phone number, they get the message "Enter a valid phone number (e.g. +353861234567)"
    - Each error above is also accompanied by an error message under the navbar of "We were unable to take payment with that card".
- Check that if the user successfully submits the Payment Details form they are redirected to the Drinks page with the following success message displayed under the navbar "You have successfully paid".
- Review of all functionality and responsiveness on mobile screen size by using [Responsinator](https://www.responsinator.com/).

#### Test Search
- Check that if the user is not logged in creating a search in the search bar will bring them to the login page.
- Check that if a login in users enters a search term in the search box and clicks the search button that the search results are presented on the product.html page correctly.

#### Test Registration
- Check that the form will only submit when all fields are populated and when the email field container a valid email type entry.
- Check that when an email that has already been used by another user is entered the error message "Email address must be unique." is display"
- Check that when a username, that has already been used by another user, is entered the error message "A user with that username already exists." is display"
- Check that when the Password and Password Confirmation fields have different entries that the error message "Passwords must match." is displayed.
- Check that when the user submits a completed registration form, they are redirected to the home page where there is a success message of "You have successfully registered!" underneath the navbar.
- Check that the button under the form area is labelled "Login". Check that the button brings the user to the correct location.
- Review of all functionality and responsiveness on mobile screen size by using [Responsinator](https://www.responsinator.com/).

#### Test Login
- Check that when the user enters an incorrect username and password combination that the error message "Your username or password is incorrect. Note that both fields may be case-sensitive." is displayed under the navbar.
- Check that when the user submits a completed login form, they are redirected to the home page where there is a success message of "You have successfully logged in!" underneath the navbar.
- Check that the button under the form area is labelled "Register". Check that this button brings the user to the correct location.
- Review of all functionality and responsiveness on mobile screen size by using [Responsinator](https://www.responsinator.com/).

#### Test Contact
- Check that all form fields are required to submit the contact form.
- Check that the initial user data (username and email) are loaded into the form fields if the user is logged in.
- Check that on successful submission of the form the user is redirected to the home page with the following success message displayed under the navbar "Thank you for your message, we will be in touch shortly!".
- Review of all functionality and responsiveness on mobile screen size by using [Responsinator](https://www.responsinator.com/).

#### Test About
- Check that the text is displaying correctly on the page.
- Review responsiveness on mobile screen size by using [Responsinator](https://www.responsinator.com/).

#### Known Issues
It was observed during testing that it would be from a design standpoint if the Drinks page didn't reload after clicking the "Add" button for an item. This results in the unfiltered Drinks page being reload instead of the filter applied by the user. This will be address in a future development sprint.

### Automated Testing

#### Python Testing

Using Django's built in TestCase Class, 43 tests were written in order to test views, form, model and apps in each of the site's modules. 

#### Coverage

To ensure that at least 80% of this projects code was tested, [Coverage.py](https://coverage.readthedocs.io/en/v4.5.x/#) was used to measure the testing done. 

The final project achieves Coverage of **86%**. 

[Coverage.py](https://coverage.readthedocs.io/en/v4.5.x/#) is include in the projects [requirements.txt](requirements.txt) and is loaded with the other requirements when run. 

To run [Coverage.py](https://coverage.readthedocs.io/en/v4.5.x/#) follow these steps:
- Execute the following command in the CLI terminal:

    ```
    coverage run
    ``` 

- On Gitpod to limit the results of coverage to just the relevant files the following command was executed:

    ```
    coverage run --omit=*/site-packages/*,*/migrations/* manage.py test
    ```
- A coverage report of the testing achieved in the project can then be generated using the following command:
    ```
    coverage report
    ```
- The final report for project is summarized  below:

<details>
<summary>Click here to see a summary of the <b>Coverage Report</b></summary>

| **Name** | **Stmts** | **Miss** | **Cover** |
| :--- | :---: | :---: | ---: |
| *accounts/__init__.py* | 0 | 0 | **100%** |
| *accounts/forms.py* | 29 | 1 | 97% | 
| *accounts/test_forms.py* | 16 | 0 | 100% | 
| *accounts/test_models.py* | 0 | 0 | 100% | 
| *accounts/test_views.py* | 53 | 0 | 100%
| *accounts/urls.py* | 4 | 0 | 100% | 
| *accounts/urls_reset.py* | 3 | 0 | 100% | 
| *accounts/views.py* | 40 | 20 | 50% | 
| *booking/__init__.py* | 0 | 0 | 100% | 
| *booking/admin.py* | 30 | 17 | 43% | 
| *booking/apps.py* | 3 |  0 | 100% | 
| *booking/form.py* | 38 | 8 | 79% | 
| *booking/models.py* | 22 | 0 | 100% | 
| *booking/test_apps.py* | 7 | 0 | 100% | 
| *booking/test_forms.py* | 10 | 0 | 100% | 
| *booking/test_models.py* | 16 | 0 | 100% | 
| *booking/test_views.py* | 16 | 0 | 100% | 
| *booking/tests.py* | 4 | 0 | 100% | 
| *booking/urls.py* | 3 | 0 | 100% | 
| *booking/views.py* | 30 | 16 | 47% | 
| *cart/__init__.py* | 0 | 0 | 100% | 
| *cart/apps.py* | 3 | 0 | 100% | 
| *cart/contexts.py* | 13 | 4 | 69% | 
| *cart/test_app.py* | 7 | 0 | 100% | 
| *cart/test_views.py* | 18 | 0 | 100% | 
| *cart/urls.py* | 3 | 0 | 100% | 
| *cart/views.py* | 24 | 16 | 33% | 
| *checkout/__init__.py* | 0 | 0 | 100% | 
| *checkout/admin.py* | 9 | 0 | 100% | 
| *checkout/apps.py* | 3 | 0 | 100% | 
| *checkout/forms.py* | 16 | 0 | 100% | 
| *checkout/models.py* | 38 | 2 | 95% | 
| *checkout/test_app.py* | 7 | 0 | 100% | 
| *checkout/test_forms.py* | 14 | 0 | 100% | 
| *checkout/test_views.py* | 29 | 0 | 100% | 
| *checkout/urls.py* | 3 | 0 | 100% | 
| *checkout/views.py* | 41 | 20 | 51% | 
| *custom_storages.py* | 6 | 0 | 100% | 
| *env.py* | 7 | 0 | 100% | 
| *main/__init__.py* | 0 | 0 | 100% | 
| *main/settings.py* | 51 | 2 | 96% | 
| *main/urls.py* | 13 | 0 | 100% | 
| *manage.py* | 13 | 6 | 54% | 
| *pages/__init__.py* | 0 | 0 | 100% | 
| *pages/apps.py* | 3 | 0 | 100% | 
| *pages/forms.py* | 7 | 0 | 100% | 
| *pages/test_app.py* | 7 | 0 | 100% | 
| *pages/test_views.py* | 22 | 0 | 100% | 
| *pages/urls.py* | 3 | 0 | 100% | 
| *pages/views.py* | 20 | 6 | 70% | 
| *products/__init__.py* | 0 | 0 | 100% | 
| *products/admin.py* | 3 | 0 | 100% | 
| *products/apps.py* | 3 | 0 | 100% | 
| *products/models.py* | 15 | 0 | 100% | 
| *products/test_app.py* | 7 | 0 | 100% | 
| *products/test_models.py* | 6 | 0 | 100% | 
| *products/test_views.py* | 39 | 0 | 100% | 
| *products/urls.py* | 3 | 0 | 100% | 
| *products/views.py* | 15 | 0 | 100% | 
| *search/__init__.py* | 0 | 0 | 100% | 
| *search/apps.py* | 3 | 0 | 100% | 
| *search/test_app.py* | 5 | 0 | 100%
| *search/test_views.py* | 16 | 0 | 100%
| *search/urls.py* | 3 | 0 | 100%
| *search/views.py* | 7 | 0 | 100%
| **TOTAL** | **829** | **118** | **86%** |

</details>

- To present the coverage report in html format (for ease of viewing) the following command was run after a report was generated:
```
coverage html 
```

- This command creates a folder called "htmlcov" which holds an "index.html" file. Running or previewing this file give a visual representation of the code that is covered by the test written.

#### Travis
In addition to TestCase and coverage.py tests, [Travis-CI](https://travis-ci.org/) was used to test Continuous Integration.

The current status of Travis for this project is as follows:

[![Build Status](https://travis-ci.org/DarrenCoppinger/milestone-project-4.svg?branch=master)](https://travis-ci.org/DarrenCoppinger/milestone-project-4)

Please note that at the time of submission this badge was marked as passing.

## Deployment

This project is currently live on Heroku : [BarTender](https://bartender-ms4.herokuapp.com/)

It should be noted that during the course of the development of this project static and media files were not uploaded to  GitHub. This was achieved by adding the folder names to the .gitignore file. The reason for this is that Heroku can't host these files. As this is the case, they are hosted from an AWS S3-Bucket. The static folder was only pushed to this GitHub repository for the purposes of project assessment by Code Institute.

### Local Deployment
To run this project locally on any system the following will need to be installed:
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
9. Set up a free account on AWS to create an S3-Bucket to service the static files for the website. 
    - Set the CORS configuration as follows:
        ```
        <?xml version="1.0" encoding="UTF-8"?>
        <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
        <CORSRule>
            <AllowedOrigin>*</AllowedOrigin>
            <AllowedMethod>GET</AllowedMethod>
            <AllowedMethod>HEAD</AllowedMethod>
            <MaxAgeSeconds>3000</MaxAgeSeconds>
            <AllowedHeader>Authorization</AllowedHeader>
        </CORSRule>
        </CORSConfiguration>

        ```

    - Create a "Bucket Policy" setting it equal to the following (Please note that you should replace the `arn:aws:s3:::bucket-name-example/*`  with your specific AWS bucket ARN. It is also important to keep the `/*` at the end of the address.):
        ```
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "PublicReadGetObject",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::bucket-name-example/*"
                }
            ]
        }
        ```
10. Go to the IAM application available in AWS. 
    - Set up a new Group. 
    - Associate the S3 Bucket you have created with this group.
    - Create a new policy by importing the "AmazonS3FullAccess" Policy, then add the ARN from the S3-Bucket to the "Resource" list. The policy should follow the following example:
        ```
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "s3:*",
                    "Resource": ["arn:aws:s3:::bucket-name-example", "arn:aws:s3:::bucket-name-example/*"]
                }
            ]
        }
        ```
    - Create a new User and associate this with the Group you have created. This will generate the following AWS access keys:
        - AWS_ACCESS_KEY_ID
        - AWS_SECRET_ACCESS_KEY

11. To push all static and media files to the S3-Bucket, run the following in your CLI terminal:
    ```
    python3 manage.py collectstatic
    ```
12. Set up a free account on Stripe and in the developer section generate test API keys. These include:
    - Publishable key = "pk_test_..."
    - Secret key = "sk_test_..."
13. Set up free account on EmailJS, add an email service (e.g. GMAIL) and create a template for your contact form. 
    - Set the template fields equal to the following:
        - To email = "<your_email_address>, {{from_email}}"
        - From name = "{{from_name}}"
        - From email = "{{from_email}}"
        - Subject = "BarTender Contact Form - {{from_name}}"
        - Content = "{{contact_request}}  {{from_name}} can be contacted at {{from_email}}."
    - Then from the Installation section of EMAILJS copy user ID generated for you in the code snippet (<your_emailjs_user_id>). 
14. Generated a env.py file where you will store your environmental variables:
    - SERCRET_KEY
    - STRIPE_PUBLISHABLE
    - STRIPE_SECRET
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - EMAILJS_USER
15. Set the SERCRET_KEY to your preferred value. 
16. Run the application by typing the following command into the CLI:
    ```
    python3 manage.py runserver
    ```
17. Running Django should generate a SQLite3 database file "db.sqlite3".
18. Migrate the structure of the database design for this project to the new database with the following commands:
    ```
    python3 manage.py makemigrations`
    python3 manage.py migrate
    ```
19. Create a superuser as follows, in order to access the Django Admin Panel:
    ```
    python3 manage.py createsuperuser
    ```

### Remote Deployment on Heroku
This app is currently deployed on heroku. The deployment is the code stored on the master branch of the project on GitHub. 

To deploy this project to Heroku required the following steps:
1. Register for Heroku and once signed in click the "New" button on the dashboard to create a new app.
2. In Heroku Name the app and specify the region (Europe in my case). 
3. Create a requirement.txt file to allow Heroku to install the required dependencies to run the app. The CLI text to input is as follows 
    ```
    pip3 freeze --local > requirements.txt
    ```
    - The requirements for this project can be found in this repositories files here: [requirements.txt](requirements.txt)
4. Create a Procfile to inform Heroku what type of app is being deployed 
    ```
    echo web: gunicorn <project_name>.wsgi:application
    ```
    - This projects Procfile can be found here: [Procfile](Procfile)
5. On the deployment tab of your project in Heroku click the Heroku GIT method for deployment (alternatively you can click "GitHub", connect Heroku directly to the repository and enable automatic deployments in the "Automatic deploys" section).
6. In the CLI of you IDE input the following:
    ```
    $ heroku login
    $ heroku git:remote -a <BarTender>
    $ git push heroku master
    ```
7. In the resources panel of Heroku type Postgres into the Add-ons search bar and then click the Provision button to add this as a resource. This will create the "DATABASE_URL" variable in the Heroku setting section under the "Config Vars" subsection.
8. Set up a free account on AWS to create an S3-Bucket to service the static files for the website. 
    - Set the CORS configuration as follows:
        ```
        <?xml version="1.0" encoding="UTF-8"?>
        <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
        <CORSRule>
            <AllowedOrigin>*</AllowedOrigin>
            <AllowedMethod>GET</AllowedMethod>
            <AllowedMethod>HEAD</AllowedMethod>
            <MaxAgeSeconds>3000</MaxAgeSeconds>
            <AllowedHeader>Authorization</AllowedHeader>
        </CORSRule>
        </CORSConfiguration>

        ```

    - Create a "Bucket Policy" setting it equal to the following (Please note that you should replace the `arn:aws:s3:::bucket-name-example/*`  with your specific AWS bucket ARN. It is also important to keep the `/*` at the end of the address.):
        ```
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "PublicReadGetObject",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::bucket-name-example/*"
                }
            ]
        }
        ```
9. Go to the IAM application available in AWS. 
    - Set up a new Group. 
    - Associate the S3 Bucket you have created with this group.
    - Create a new policy by importing the "AmazonS3FullAccess" Policy, then add the ARN from the S3-Bucket to the "Resource" list. The policy should follow the following example:
        ```
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "s3:*",
                    "Resource": ["arn:aws:s3:::bucket-name-example", "arn:aws:s3:::bucket-name-example/*"]
                }
            ]
        }
        ```
    - Create a new User and associate this with the Group you have created. This will generate the following AWS access keys:
        - AWS_ACCESS_KEY_ID
        - AWS_SECRET_ACCESS_KEY

10. To push all static and media files to the S3-Bucket, run the following in your CLI terminal:
    ```
    python3 manage.py collectstatic
    ```
11. Set up a free account on Stripe and in the developer section generate test API keys. These include:
    - Publishable key = "pk_test_..."
    - Secret key = "sk_test_..."
12. Set up free account on EmailJS, add an email service (e.g. GMAIL) and create a template for your contact form. 
    - Set the template fields equal to the following:
        - To email = "<your_email_address>, {{from_email}}"
        - From name = "{{from_name}}"
        - From email = "{{from_email}}"
        - Subject = "BarTender Contact Form - {{from_name}}"
        - Content = "{{contact_request}}  {{from_name}} can be contacted at {{from_email}}."
    - Then from the Installation section of EMAILJS copy user ID generated for you in the code snippet (<your_emailjs_user_id>). 
13. In the Heroku settings tab, click on the "Real Config Vars" button to set environmental variables as follows:
 - AWS_ACCESS_KEY_ID: `<your_aws_key>`
 - AWS_SECRET_ACCESS_KEY: `<your_secret_aws_key>`
 - DATABASE_URL: `<postgres_database_link>`
 - DISABLE_COLLECTSTATIC: `1`
 - EMAIL_ADDRESS: `<your_email_address>`
 - EMAIL_PASSWORD: `<your_email_password>`
 - SERCET_KEY: `<your_secret_key>`
 - STRIPE_PUBLISHABLE: `<your_stripe_publishable_key>`
 - STRIPE_SECRET: `<your_stripe_secret_key>`
 - EMAILJS_USER: `<your_emailjs_user_id>`
 
14. Migrate the structure of the database design for this project to the new database with the following commands:
    ```
    python3 manage.py makemigrations`
    python3 manage.py migrate
    ```
15. Create a superuser as follows, in order to access the Django Admin Panel:
    ```
    python3 manage.py createsuperuser
    ```
16. In the top right of the Heroku dashboard press the "Open App" button to view your deployed Heroku app.

## Credits
### Media
Images used in this site were sourced from the [Wikimedia Commons](https://commons.wikimedia.org/).

### Acknowledgements
- [Antonio Rodriguez](https://github.com/AkaAnto) my Code Institute mentor for his supervision and input.
- All the Code Institute Tutors for their help and support during the development of this project and my other milestone projects.

### Disclaimer
This Website was produced for educational purposes only.