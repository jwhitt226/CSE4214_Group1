# Software Requirements Specification
### for
# Bookaholics
### Version 1.0 approved
### Prepared by Justin Whittington, Landyn Sullivan, Marquasia Smith, Mykenzie Strickland, Kenneth Mack
### Department of Computer Science, Mississippi State University
### January 26, 2024
# 1. Introduction
## 1.1 Purpose
This document, version 1.0, serves as a comprehensive outline of the software requirements for the online bookstore, "Bookaholics." It provides a detailed product description, as well as a framework to be utilized by the development team. This is accomplished by covering the entire Bookaholics system, including user interactions, interface functionalities, information storage, database management, and security. In doing so, the document should act as the foundation and guide necessary for fulfilling the intended expectations of the final product.
## 1.2 Document Conventions
## 1.3 Intended Audience and Reading
This document is primarily written for the CSE 4214 Group 1 development team, with additional relevance to faculty and teaching assistants overseeing the project. Section two of this document provides a product description, encompassing functions, user classes, and product restraints. Sections three and four describe system features and nonfunctional requirements. The bulk of the software architecture can be derived from these two sections in particular. They are expected to serve as crucial references for the development team and provide ongoing guidance as the project evolves. Section five covers miscellaneous requirements which did not fall into either of the two other categories.
## 1.4 Product Scope
Bookaholics is an online bookstore dedicated to the seamless sale and distribution of books. It aims to act as a platform for both casual readers and literature enthusiasts to explore, browse, and purchase books of all kinds. Approved publishers and distributors act as sellers, connecting directly with buyers seeking their products. Bookaholics is geared towards ease of use, accessibility, and product diversity. Key functionalities include robust search and browsing features, personalized user accounts, suggestions based on previous purchase history, and a secure check out process. 
## 1.5 References
# 2. Overall Description
## 2.1 Productive Perspective

*Bookaholics* is a web application that allows the purchasing and selling of books. It is a new self-contained product that will be developed by using frontend and backend programming. The front-end will allow users to physically interact with the web application, and the backend will allow engineers to store and maintain all-important data regarding the application. Our engineers will utilize the programming languages Python, SQL, HTML, CSS, and JavaScript for the development of the web application.

## 2.2 Product Functions

* All users will be able to create an account

* All users will have the ability to log in and out of the application

* Users will be able to search the inventory, but only the admin will be able to manage the inventory

* Buyers can add, remove, view, and check out cart

## 2.3 User Classes and Characteristics

*Bookaholics* is an application that is designed for many user types. The most important users that will interact with the application are buyers, sellers, and admins. Depending on the user type, there will be certain authorizations allowed that other users will not have access to. For instance, admins will have the authority to approve or disapprove sellers within the application, but the other user types will not have this specific ascendancy. On a scale from most important to satisfy to least important, buyers will be considered the most important, as they will be purchasing and utilizing the web application the most. Overall, all the users are important and have specific characteristics, but the buyers are the main users that we would like to please first, then sellers and admins will follow.

## 2.4 Operating Environment

The web application will operate on Windows and Mac OS servers, in which it will be able to be accessed through Internet Explorer.

## 2.5 Design and Implementation Constraints

With the development of *Bookaholics*, there will be a few limitations. The application will only be available in English. This indicates that anyone who does not speak or understand the English language will not be able to interact with the web application. Another limitation for the web application will be accessibility. The development of *Bookaholics* will not be designed in a way that will be accessible for individuals who may have difficulty utilizing technology traditionally. For example, users who are visually impaired or lack fine motor skills. Lastly, depending on the user's environment, internet connectivity may play a substantial role in the usage of *Bookaholics*.
# 3. System Features
## 3.1 Administrative Page
### 3.1.1 Description
An administrator will have a unique page which will allow them to remove listings, authorize seller accounts, remove an accounts “seller” status, remove accounts, and authorize return requests.
### 3.1.2 Stimulus
The administrative page will show current sellers and pending seller requests and allow the admin to accept, decline, or remove sellers. The admin will also be able to remove listings on the “browse listings” page, as well as remove accounts, and authorize return requests.
### 3.1.3 Functional Requirements
- 3.1.3.1	The admin will be able to accept sellers.
- 3.1.3.2	The admin will be able to decline sellers.
- 3.1.3.3	The admin will be able to remove sellers.
- 3.1.3.4	The admin will be able to remove listings.
- 3.1.3.5	The admin will be able to remove accounts.
- 3.1.3.6	The admin will be able to authorize return requests.
## 3.2 Modify Seller Listings
### 3.2.1 Description
A seller should be able to post and remove different book listings as well as view their current listings.
### 3.2.2 Stimulus
The seller should be able to post and remove different book listings as well as view their current listings.
### 3.2.3 Functional Requirements
- 3.2.3.1	The seller should be able to view their current listings.
- 3.2.3.2	The seller should be able to remove listings.
- 3.2.3.3	The seller should be able to add listings.
## 3.3 Profile Management
### 3.3.1 Description
Allow the user to edit their profile information and apply to be a seller in the system.
### 3.3.2 Stimulus
On the user’s home screen, they should be provided with an edit profile button that will allow them to change their information. They should also be able to apply to be a seller, though this will need to be authenticated by an admin.
### 3.3.3 Functional Requirements
- 3.3.3.1	Allow the user to edit their profile information.
- 3.3.3.2	Allow the user to apply to be a seller.
## 3.4 User Registration
### 3.4.1 Description
Allows the user to register an email and password pair with the system and allow the user to login using a registered email and password pair.
#### 3.4.2 Stimulus
The user will be given a register option on the login screen. Clicking the register button will take the user to a screen where they will need to register using their email address, name, mailing address, password, and payment information. This information will then be stored in a database. The user should also be given an input box for an admin code and if the code is valid, they will be registered as an admin. A registered user should be able to login using their email and password, the system will then validate that email/password pair and take the user to their home screen.
### 3.4.3 Functional Requirements
- 3.4.3.1	The system should display a screen for the user to enter their email address, name, mailing address, password, and payment information. 
- 3.4.3.2	The system should store the user’s information in a secure database.
- 3.4.3.3	The system should validate the admin code and register the user as an admin if necessary.
- 3.4.3.4	The system shouldn’t allow the user to register without filling in the email address, password, mailing address, and payment information fields.
- 3.4.3.5	The system should display a login screen with input boxes for email and password, as well as a login button.
- 3.4.3.6	The system should validate and email and password pair and throw an error if invalid.
## 3.5 Browse Listings
### 3.5.1 Description
Allows the user to search for books by titles, authors, and ISBN numbers. The user can also browse by genre and click on books to view more information.
### 3.5.2 Stimulus
A user will use a search bar to search for a specific book by title, author, or ISBN number. The system will then search for books that are correlated with that title or author and display the results to the user. The user can also select a genre from a selection of genres to browse through.
### 3.5.3 Functional Requirements
- 3.5.3.1 The system should display a search bar that the user can type in. 
- 3.5.3.2 The system should display a search button that the user can click to initiate a search. 
- 3.5.3.3 The system should provide the user with the search results. 
- 3.5.3.4 The system should display an error if there are no listings that match the user’s search. 
- 3.5.3.5 The system should also provide a menu of genres for the user to select. 
- 3.5.3.6 The system should only show items that match the genre selected by the user. 
- 3.5.3.7 The system should return search results in order with the items with the closes match with the search appearing first. 
- 3.5.3.8 The user should be able to click on a book to see more information on it. 
## 3.6 Modify Cart
### 3.6.1 Description 
Users should be able to view their cart and add and remove items from their cart before continuing with the checkout process. 
### 3.6.2 Stimulus 
The user will click an “add to cart” button, and the system will add the item to a list of items that are to be purchased later. Alternatively, the user can click a “remove from cart” button that will remove an item that was previously added to the cart. The user can also click a “view cart” button to access their cart. 
### 3.6.3 Functional Requirements 
- 3.6.3.1 The user should be able to access their cart through a button. 
- 3.6.3.2 The system should allow users to add books to their cart. 
- 3.6.3.3 The system should allow the users to remove books from their cart. 
## 3.7 Checkout
### 3.7.1 Description 
User should be able to formally purchase all items currently present in their cart. They will pay the seller who listed each individual item via payment information that has already been stored in their account.  
### 3.7.2 Stimulus 
While viewing the cart, user will select the “Check Out” option. The system will calculate and provide an estimated total, as well as the list of items currently in that users cart. The user will select the “Place Order” option. The system will verify the payment method provided, pass the order along to the respective sellers, and reduce inventory as needed. Alternatively, if the payment method cannot be validated, the user will be notified via email and the order will not be placed. 
### 3.7.3 Functional Requirements 
- 3.7.3.1 User will be able to access checkout menu through a button. 
- 3.7.3.2 User will be able to place order via a button. 
- 3.7.3.3 System will be able to calculate and provide estimated total. 
- 3.7.3.4 System will be able to verify payment method. 
- 3.7.3.5 System will be able to pass order to the necessary sellers. 
- 3.7.3.6 System will be able to manipulate inventory accordingly. 
## 3.8 Return Items
### 3.8.1	Description  
Users should be able to return items back to the seller that they previously purchased. Once the item is returned, the user will receive payment via store credit. 
### 3.8.2	Stimulus/Response Sequences 
The user will submit a return request, and the request will be reviewed and accepted or denied. Once the request is accepted and the seller confirms the item has been returned, the user will get their money back via store credit. 
### 3.8.3	Functional Requirements 
- 3.8.3.1 User should be able to submit a return request. 
- 3.8.3.2 Seller should be able to confirm receipt of the return. 
- 3.8.3.3 User should be refunded  via store credit. 
# 4. Other Nonfuntional Requirements
## 4.1 Perfromance Requirements
Bookaholics can be accessed through a web server. Therefore, the timing of website will rely on the stability and connection of the user’s internet, and it will also be based on the capabilities of the hardware that the user is using.
## 4.2 Safety Requirements
Bookaholics will have password requirements when the user sets up their account to aid in preventing the user’s information from being stolen. It will require the user to create a password that is at least 8 characters long and contains an uppercase letter, a lowercase letter, and a special character.
## 4.3 Secruity Requirements
To ensure the security of the user’s information:
- The user's password will not be displayed. If the user cannot remember their password, there will be a reset password option.
- The user’s credit card number will not be displayed after adding the payment method. After the user sets a card as a payment method, the website will only display the last 4 digits of the card number, so the user can identify that it is the payment method they will be using to pay.
- Transactions through the website should be secure and protect the user's information.
- The user will have 7 attempts to enter in the correct password until their account is locked. The user will have to reset their password to unlock their account.
## 4.4 Software Quality Attributes
Bookaholics should be viewed through a device that has an active internet connection. The website should be easy to navigate as well as use. 

The website should be reliable enough to not crash when there are multiple users on the site, and it should be reliable enough to maintain the same output for the same input from different users.
# 5. Other Requirements
