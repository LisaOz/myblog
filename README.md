# Personal Blog Application

This project is a personal blog application built with Django. It allows users to create, post and share blog posts. Users can search for posts by title and date, look for the similar content within the site, share posts via email, and write comments to the posts.

## Features

**Post Management:**
  - Create and publish blog posts.
  - Search posts by title and/or date.
  - Share posts via email.
  - Comment posts.
  - Organize posts using tagging system.
  - Mark posts as "published" or "draft" to control their visibility on site.
  - Edit, save or delete posts from the application database.

**Post Model:**
- Defined *'Post'* model with *'datetime'* field to manage creating and publication time.
- Implemented default sorting order for posts.
- Created database indexing for efficient queries.
- Added status field to manage the visibility of posts (*'published'* or *'draft'*).
- Defined many-to-one relationships to associate each post with one auther, and many-to-many relationships to allow one user to like multiple posts, and for each post to be liked by many users.

**Django Administration:**
- Created a superuser (admin) for managing the blog.
- Customised how models are dislayed in the admin interface.
- Managed user accounts: possibility to disable, remove or block users.
- Managed comments: possibility to disable or remove comments.
- Set post status: mark posts as "published" or "draft"; add, edit or delete posts.

  **QuerySet and Managers:**
  - Create and update post objects.
  - Retrieve and filter post objects using various field lookups.
  - Counter, order, and check the objects for existence.
 
  **Views and URL Patterns:**
  - Created list and detail views for blog posts.
  - Added URL patterns to map views to URLs.
  - Developed *base.html*, *post_list.html* and *post_detail.html* templates for rendering the site layout, displaying the list of blog posts and showing the details of individual posts.
  - Implemented pagination to the post list view, limiting the number of posts displayed and enabling to go to the requested page.
 
**Email Integration:**
- Enabled sending emails with Django from the post detail page with the required view.

**Comments:**
- Created a form for submitting comments to the posts.
- Displayed comments on the posts details page in the admin interface.
- Manage comments through the admin site: aprove, disable or delete.

**Tagging and Search:**
- Implemented tagging for posts.
- Added a title seach feature, implemented trigram search to allow searching posts by the initial letters of the post title, providing quick and efficient search results.
- Built a customs search view with stemming and ranking results.
- Implemented recommendation of similar posts based on shared tags, prividing users with a personalised feed of related posts.

**Additional Features:**
- Added a sitemap for better SEO.
- Implemented RSS feeds for blog posts.
- Installed and configured PostgreSQL for database management.

## Installation

To install and run this project locally:
1. Clone the repository:
   \``https://github.com/LisaOz/myblog/`\``
3. Navigate to the project directory:
   \``cd myblog`\``
4. Install dependencies:
   pip install -r requirements.txt**
5. Run database migrations:
   \``python manage.py migrate`\``
6. Create a superuser for accessing the Django admin site:
   \``python manage.py createsuperuser`\``
7. Start the development server:
   \``python manage.py runserver`\``
8. Access the application by navigating to **http://localhost:8000** in your web browser.

## Usage

1. **Creating Posts**: Navigate to the admin site to create, edit and manage blog posts.
2. **Browsing Posts**: Use the main page to browse through the list of posts.
3. **Searching**: Use the search bar to find posts by the title or content.
4. **Commenting**: On each post's detail page, users can submit comments using the provided form.
5. **Sharing Posts**: Posts can be shared vie email from the post detail page.

## Licence

Thhis project is licenced under the MIT Licence. See the 'Licence' file for more details.

## Contributing
Contributions are welcome. Please submit a pull request or open an issue for any bug report, feature request, or improvements.

## Acknowdelgements
This project is based on examples from the book *"Django 5 By Example"* by *Antonio Mele*. 
A special thanks to *Antonio Mele* for his excellent book, which provided the foundational knowledge and inspiration for this projects. This book has been an invaluable resource in understanding Django and building my first application.
