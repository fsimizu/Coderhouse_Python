# RYDE | Travel blog

### Description
Welcome to RYDE, your passport to a world of wanderlust and exploration! We are avid travelers who have embarked on a journey to share our experiences, tips, and inspirations with fellow globetrotters. Whether you're a seasoned adventurer or a first-time explorer, our travel blog is designed to ignite your passion for discovery and help you plan your next unforgettable journey.

### Table of contents

* Installation
* Usage
* Features

### Installation

1. Clone the repository: git clone https://github.com/fsimizu/Coderhouse_Python.git
2. Navigate to the project directory: e.g. cd your-travel-blog-app
3. Create a virtual environment: python -m venv venv
4. Activate the virtual environment:
    * On Windows: venv\Scripts\activate
    * On Unix or MacOS: source venv/bin/activate
5. Install dependencies: pip install -r requirements.txt
6. Apply migrations: python manage.py migrate
7. Create a superuser account: python manage.py createsuperuser
8. Run the development server: python manage.py runserver


### Usage

1. Run the development server as mentioned above.
2. Visit the blog at http://127.0.0.1:8000/ to read existing posts and create new ones by registering.

### Features

1. #### User Registration:
    Visitors can register as users to the travel blog.
    To register, users need to provide a unique username, email, name and password.

2. #### Post Creation:
    Registered users can create new travel blog posts.
    Posts include a title, subtilte, content, and an image.

3. #### Post Management:
    Users have the ability to edit and delete their own posts.
    This allows for updating and removing content as needed.

4. #### User Profiles:
    Users can customize their profiles by adding their own avatar.
    Avatars add a personal touch to user profiles and blog posts.

5. #### Authentication and Authorization:
    Secure authentication mechanisms are implemented for user login and logout.
    Authorization is in place to ensure that users can only edit or delete their own posts.

6. #### Responsive Design:
    The blog features a responsive design to provide an optimal viewing experience across various devices.

7. #### Admin Panel:
    An admin panel is available for site administrators to manage users, posts, and other content easily.

8. #### Search Functionality:
    Users can search for specific posts or topics within the travel blog.

9. #### User-Friendly Interface:
    The user interface is designed to be intuitive, making it easy for users to navigate and interact with the blog.