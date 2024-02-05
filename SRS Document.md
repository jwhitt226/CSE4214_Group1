# 1. Introduction
# 2. Overall Description
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

## 3.6 Modify Cart
## 3.7 Checkout
## 3.8 Return Items
# 4. Other Nonfuntional Requirements
# 5. Other Requirements
