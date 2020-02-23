# Miller Merchant - Milestone 4 Project

The purpose of Miller Merchant is to demonstrate a proficiency in building a Django backend project using a relational database to create 
a website that allows users to store and manipulate data.

The Miller Merchant project has two sides , the first of which is the storefront which allows the user to browse and purchase books from 
their favourite authors. The user is able to complete the entire buying process without having to leave the site. The second part of the 
project is designed to help create a community atmosphere on the site and get the users involved. Once a month a competition is created 
that allows users to vote for a book that they would like to be added to the store. Signed copies of the winning book are added once the 
competition is complete, the books and are accompanied by an interview with the author that is posted in the members only section of the 
site.

Although the two parts of the website are different, one part being a store and the other a voting competition,  it is the uniformed user 
interface and styling that makes sure that a user can browse seamlessly through the site without realising that they are  moving between 
different apps. 


## UX

The project is aimed at people who shop online, enjoy reading books and research products before making a purchase. The site allows users 
to get an understanding of what the book is about without giving away any spoilers, this should lessen the chance of a user buying a book 
and then to realise 50 pages in that it is not the type of book they like. All of the authors which have a book on the site have a bio 
page, this allows users to find out more about the author of a book they enjoyed or find out what other books they have written. The book 
of the month section of the site allows users to vote and comment on why they want a book added to the site. This promotes healthy 
competition between users and is a platform for debate. The signed copies of the winning book also appeals too collectors and as they are 
limited make them even more desirable.

The project has been designed with a mobile first approach but it is fully responsive across all devices. This has been achieved by using 
Bootstrap as a UI component library, this allows the objects on the page to be laid out differently depending on the view width of the 
device being used. There are various ways to navigate through the site thanks to using Python and Django, we believe that the majority of 
users will arrive on the home page which is the storefront listing all of the books that are available to purchase. From the homepage the 
user is able to select any of the books to get a more detailed view or navigate around other parts of the site using the nav bar, examples 
of users navigating through the site in different ways in order to achieve specific goals are listed below;
- User type newbie - A user arrives onto the site by chance after searching for a specific book on google that is listed on Miller Merchant. 
The users goal when arriving onto the site is to purchase the book they have been searching for. This is done by selecting the book on the 
storefront, adding it to cart and completing the checkout process
- User type returning customer - A user returns to the site while they are midway through a book purchased on our store as they are curious 
about the author. The users goal is to find out more about the author and possibly buy another one of the authors book. The user selects the  
book they are currently reading on the storefront which opens up a detailed view, then clicks on the authors name which is a hyperlink to a 
detailed bio of the author which includes a list of the books they have written. 
- User type competitor - A user has arrived on the site after following a link in a tweet from their favourite author which stated they might 
be able to purchase a signed copy of their new book if the author wins the competition. The user arrives on the book of the month landing page 
where it states that creating an account is a prerequisite to enter the competition. As the users goal is to vote, registering is not a 
problem. After they have done this they are able to vote for their author and let others know why they should do the same in the comment 
section.
- User type referral - A user has been recommended by a Miller Merchant customer at their book club. The user was advised to read a previous 
book of the month winning interview as it was going to be a feature book in their club and it gave a good insight as to what the author was 
thinking when they wrote the book. The goal of the user was to find information on the book which was done by registering on the book of 
the month landing page and selecting past winning interviews. 
- User type specific - A user arrives on the site after a google search, the users goal is to find a book that is short as they like to 
finish books within a week. As soon as the user arrives on the storefront they notice that each book has an estimated reading time which 
fits their needs perfectly. Once they have scrolled through the storefront and narrowed down based on reading time they can then decide 
which on eta go for and odd to cart.

Prior to the project being created there were several design ideas, this changed due to the products being sold having to changed, please 
see below in issues faced. When recommencing with the project mockups were made of all the major parts of the website. The mockup images 
are hosted on Flickr and can be viewed at https://www.flickr.com/photos/zanderm73/.


## Features

The Miller Merchant site is a complete project that has launched with all the necessary features for it to function well. All of the features 
that have been implemented are listed below, there is also a list of future features that may look to be implemented if it is deemed 
beneficial for the project moving forward.

### Existing Features
- Register/login - allows users to create an account by completing a registration form. This will allow the user carry out actions such as 
purchase items and access members only parts of the site. If products are added to cart then the user leaves the site, what was in the cart 
will be saved.
- Expanded product view - allows users to get a more in depth description of the product that they are viewing on the homepage. The user 
does this by selecting the view product button which opens up a unique product page.
- Expanded author bio - allows the user to read information about the author. The user does this by selecting the author hyperlink which is 
on the expanded product view page. This opens up a unique author page.
- Add to cart - allows the user to save products in a list while browsing by selecting the add to cart button. This list is then presented 
to the user at checkout.
- Checkout - allows the user to purchase items based on the items that they previously added to cart. They do this by completing the checkout 
process which includes entering delivery address and payment details.
- Contact Us - allows the user to contact the site admin directly by email. This is done by the user selecting the ‘contact us’ hyperlink in 
the footer which is shown on every page. This automatically opens the users default email platform and the Miller Merchant address is 
autofilled.
- Search - allows the user to search the site to see if Miller Merchant has a specific product. The user is able to do this by entering the 
title into the search bar which is part of the header and is shown on every page. When the search button is selected the user will be directed 
to a search result page.
- Vote/comment - allows the user to vote for which book they think should win the monthly competition and in turn potentially get the chance 
to purchase a signed copy of the product from the author. The comment function allows the user to express their opinion and state why they 
voted for that particular product. This part is only open to users who are registered, once they have logged in they need to navigate to the 
competition page and fill in the usercommentform. After this is done there vote will be counted and comment will be shown to all users on the 
page. 
- Extended Interviews - allows registered users to read extended interviews with book of the month winning authors. The current winning 
interview is displayed on the book review.html page which contains a link to a list of the previous winning interviews.
- Monitor Live Scores - allows the user to check on the current months competition which displays the scores live. To see the current scores 
the user needs to navigate to the view votes.html, the link for this is within the book review landing page. 

### Features To Implement
- Forum - Would allow users to have discussions with each other on a moderated platform, it would also create a good way to gain feedback 
from the users as to what they would like on Miller Merchant. This could be done by creating a forum app and using bootstrap forms
- Subscription service - Would allow registered users to be guaranteed a signed copy of the competition winners book every month if they were 
to sign up to a subscription based service which would give them priority on signed books and a discount on the store.
- Additional platforms - Would allow user to take in the information that the product has in different ways such as in a digital format to 
read on a smart device or listen to as an audio book. 
- User Profile Improvement - Would allow users to set their profile to public, in turn this would allow members to look at other members 
profiles which would contain a brief bio written by the user themselves. Also a timeline of the users actions on the site would be visible 
which would show who the voted for in competitions and what comment they made. The user would also be able to see all purchases that they 
have made on the site and check the status of their orders that are in progress.
- Social Media - allows the user to follow and interact with Miller Merchant on multiple platforms instead of just on the site. The user does 
this by selecting the instantly recognisable social media icons located in the footer.


## Technologies Used
The Miller Merchant project utilises various programming languages, libraries and frameworks which enables it to be a full stack project with 
a depth of customisation. Below are the technologies and justification as to why they were used;

Languages
- HTML - Used as the building blocks allowing text to be displayed on the project
- CSS - Used to style the website making the HTML more appealing to the user. It also allows the site admin to change multiple parts of the 
site with a small amount of code
- Python - Used as this provides increased functionality over HTML/CSS alone. A vital part of the project is the front end being able to 
display, read, input and edit information stored on the SQLite back end database, Python was used to do this (https://www.python.org/)

Frameworks/Libraries
- Stripe - Used to handle the payment process so that there is no payment details stored on the projects database when a customer is 
purchasing products (https://stripe.com/gb)
- Javascript - Used to add interactive functionality to the project such as the mobile nav bar. It is also used in the payment process when 
using Stripe (https://www.javascript.com)
- jQuery - Used to manipulate the DOM and reduce the amount of code required compared to using javascript alone, shortening the development 
time (https://jquery.com/)
- Django - Used as it provides a model-template-view structural architecture. Django also provides projects with an admin page where the site 
admin can create, delete and edit data stored on databases that the project uses https://www.djangoproject.com/. 
- Bootstrap - Used to ensure that the project based on a mobile first approach. Bootstrap allows an enhanced level of customisation compared 
to standard HTML for an improved user experience. The Bootstrap library also contains form layouts which are used at throughout the site 
(https://getbootstrap.com/).

Databases
- SQLite - Used to store data  during development that is essential to the project such as the product information. Also stores user data 
such as profile info, vote selection and comments that they make (https://www.sqlite.org/index.html).
- PostgresSQL - This was used in place of SQLite when the project was deployed (https://www.postgresql.org/).
- AWS S3 - Amazon AWS was used to store static files such as the css file and also the media that the project needed such as product and 
author pictures(https://aws.amazon.com/).


## Testing

Various methods of testing were carried out throughout the building of the project and further testing was carried out once Miller Merchant 
had been deployed using Heroku. Below is the explanation of what testing was done and why;

### Automated Testing

### Manual Testing
- Accessing and navigating the site on multiple browsers
	1.  Accessing Miller Merchant using the different browsers to ensure that everything is displayed correctly. The browsers used were 
    safari, chrome and internet explorer. 
	2. 	All links in the nav bar and footer were selected to make sure they were all live. This was done while logged in being a registered 
    user and browsing as a guest.
	3. 	The detailed product view button on the storefront was tested when in the detailed view the author bio link was tested. All back 
    buttons to get the user back to the storefront were tested.
	4.	The book of the month section was tested by walking through each part after arriving on the landing page. All buttons were linked 
    to the correct pages.
- Registering/logging into an account
	1.	Following the steps of registering as a new user would have too, selected register in the nav bar and completed the registration form 
    that is contained in the page that the user is directed too. After a successful registration the home page was loaded with a success 
    message below the nav bar.
	2.	 Logged into the site as a registered user, selected login in the nav bar and completed the form which asked for users email and 
    password. The homepage was then loaded with a success message under the nav bar to let the user know they are now logged in.
- Adding to cart and purchasing
	1.	Logged into the site, selected a book on the storefront, selected one copy of the book by pressing add to cart. It can be validated 
    that this is added to cart as the quantity of items in the cart appears next to cart in the nav bar.
	2.	Selected cart in the nav bar that directed to to cart page, once items and quantity were correct proceeded to checkout using the 
    button. Directed to delivery and payment forms. Once valid information had been input into the forms the submit button was selected. This 
    redirected to the storefront homepage with a message under the nav bar stating that the payment was made and order will be processed.
- Voting for book of the month, checking unique_together constraint and checking other users comments
	1.	Logged into the site, navigated to the book of the month landing page,  selected ‘vote for book of the month’ button. Selected the 
    book from the dropdown, commented as to why this book was chosen and submitted vote. Navigated back to the book of the month main page 
    via the nav bar, selected ‘live book voting score’ which opened up view votes.html which showed comments made by users and there was a 
    tally of the current competition scores.
	2.	Navigated back to the voting form and tried to submit another vote for the same book which failed as designed, an error message 
    appeared under the nav bar stating that I had already voted this month.
- Project viewport response
	1. Navigating the site on multiple devices with various viewports. Devices tested were MacBook Pro 13 inch, iPad Air 2, iPhone 5S, Samsung 
    Galaxy S9+.

### Stripe Payment Testing
To use the dummy payment function on Miller Merchant please use the details below as these have been tested. Note that this will not actually 
charge a card and no goods will be sent, this is for development purposes only;
- Card number - 4242 4242 4242 4242
- CVV - Any 3 digit combination
- Expiry date - Any date that after this current month

### Automated Testing 
- Automated testing was done by using Djangos testing framework. To run the tests ‘’python3 manage.py test’’ was entered into the command line.
- Travis CI (https://travis-ci.org/) was also used as a means of automated testing. This ensured that all of the required dependancies were 
included in the build to allow others to use the project without them having to search for additional programs that their machine might not 
have. The ‘build passing’ icon below confirms that the most current build is passing. The only additional information that users would need 
to input is environment variables which are described further in the deployment section.
[![Build Status](https://travis-ci.org/zanderm73/milestone4-miller-merchant.svg?branch=master)](https://travis-ci.org/zanderm73/milestone4-miller-merchant)

### Validation Services 
- All HTML code was tested using the W3C HTML tool validator ( https://validator.w3.org). The validator stated that the class attribute was 
duplicated but this was used to differentiate and customise different parts of the project.
- All CSS code was tested using the W3C CSS tool validator (https://jigsaw.w3.org/css-validator/). The only error found was the 
background-color was stated as none. None was declared to override any bootstrap themes changing the color.

## Issues Faced
While developing the Miller Merchant project there were issues that lead to an increased completion time. When creating a project of this 
size while still learning about many of the technologies being used it was inevitable that there would be stumbling blocks, listed below is 
an explanation of the issues faced;
- Initially the product group was going to be building materials but this had to be changed during the development due to a conflict with my 
current job. The issue was overcome by changing the product group to books and changing a number of models. This was a big setback as many of 
the features that were going to be implemented were unique to building products and not suitable to be used on a project where the product 
focus was physical books. I.e. R-value calculator that  works out the resistance value of the build up once multiple products have been 
selected to make up a wall, floor or ceiling.
- The project was initially developed on the AWS IDE platform as this had been used to complete the previous project after Cloud9 had been 
acquired by Amazon. As the project developed it was clear that there were some major issues when using AWS IDE. The biggest of which was the 
amount of token hours provided by AWS to Code Institute students. The token hours reduced even on days that the platform was not used, there 
was also no information stating what happened when the token hours reduced to zero and if it was possible to top up the hours by payment. 
This led to speculation on Slack that once an account went to zero it would be locked and the work contained in AWS IDE would be inaccessible. 
Many of the users having issues with AWS IDE who were posting on Slack and Stackoverflow were moving to Gitpod and recommending it to others. 
This led to the Miller Merchant project being developed using Gitpod, the platform is very easy to use and seems to gaining in popularity.


## Deployment
The project has been deployed using Heroku. All environment variables that were stored locally during development were not were not pushed to 
GitHub due to security reasons. This resulted in the environment variables during deployment being stored as config VARs within the app on 
Heroku, these will remain private. 
Heroku does not support file uploads which leads to any images uploaded being deleted when the app is restarted. Amazon AWS S3 is used to 
store static files and media files. All of the deployed images are hosted by S3. The process of deploying was straightforward due to Heroku 
being able to pull the most recent GitHub commit and AWS Identity and Access Management providing keys to securely host the projects static 
data.

To run this project on another machine, an IDE such as Gitpod with PIP, Git and Python3 installed would be required. The project can be cloned 
from GitHub using the HTTPS link. All other packages that are required to be installed are located in the requirements.txt file and can be 
installed using the command ‘pip -r requirements.txt’. An env.py file needs to be created in the IDE to store the following variables;
- SECRET_KEY - Take from your own settings.py file
- STRIPE_PUBLISHABLE - API keys will be given once a stripe account is setup 
- STRIPE_SECRET - API keys will be given once a stripe account is setup 
- EMAIL_ADDRESS  - Your current email
- EMAIL_PASSWORD
- AWS_ACCESS_KEY_ID - The keys will be given once the AWS bucket is setup, media and static files will be stored here using AWS S3
- AWS_SECRET_ACCESS_KEY


## Credits

### Content 
The book images were obtained from the website world of books (https://www.worldofbooks.com/en-gb). The author images were obtained via google 
search images (https://www.google.com/?&hl=en). The summary/reviews of the books were taken from multiple sources such as Wikipedia, Amazon 
and worldbooks.

### Code
The initial layout of the project home page, checkout and menu was taken from the Code Institute Bootcamp and Code Institute tutorial, this 
was used as a base which was later heavily redesigned throughout development process. The registration/login feature and search bar were taken 
from the e-commerce mini project in the Code Institute tutorial, they may be slightly different as the features that have been implemented 
were written by myself, Alexander Miller while following the tutorials. The password handling, reset and email confirmations were also taken 
form the mini tutorial prior to this milestone project. The handling of card payments and the stripe checkout process was also taken from the 
tutorials while working through the full stack fundamental course.

### Acknowledgments
This project was created for the Milestone 4 project during the Code Institute Full Stack Development course by Alexander Miller. A lot of 
the technologies used in the project were introduced and taught by the Code Institute team throughout their tutorials. Many of the issues 
faced were solved by using the Code Institute Slack channel or Stackoverflow.
