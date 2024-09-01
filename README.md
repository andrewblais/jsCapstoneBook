# **jsCapstoneBook**

_A Node.js Web App where users add books and comments to a reading club list. Capstone Project completed for Angela Yu's Udemy Web Development Bootcamp._

## **_Requirements:_**

-   Download and setup the software required for a local database:

    -   https://www.pgadmin.org/

    -   https://www.postgresql.org/

-   Fork/download this repository, `jsCapstoneBook`.

-   Here are the standard steps/commands I intially use to create the Node.js/Express project...

-   Install Node.js: https://nodejs.org/en

-   In the Bash terminal, install the necessary Node.js libraries/resources:

```bash
npm init -y
npm install
npm install pg
npm install express
npm install body-parser
npm install ejs
npm install dotenv
```

-   The project directory structure should look something like this:

```
├───jsCapstoneBook
    ├───node_modules
    │   ├───...
    ├───public
    │   ├───assets
    │   │   └───icons
    │   ├───images
    │   └───styles
    └───views
        └───partials
```

-   Add `"type": "module",` to `package.json` file

## **_Background:_**

-   This project is the culmination of a lot of hard work. I strive to understand, visualize and complete this project/assignment from Angela Yu's Web Development Bootcamp with thoroughness, accuracy and creativity.

-   I began studying Python, Web Development with Python, Math and Data Science in 2022 and have completed two Python Bootcamps and one Python/Math course, and am now taking Linear ALgebra and Statistics/Machine Learning with Python courses. I added JavaScript Coding and Web Development to my curriculum in 2023. The goal is to have a solid foundation of General Software development in both languages, and also to be versed in Front and Backend Web Development. Ultimately I'd like to contribute to the A.I. Alignment Discussion.

-   So far things are going well. I'm very comfortable with Python, and getting there with JavaScript. It's also helpful that I'm concurrently taking Colt Steele's JavaScript course on Udemy. This Capstone Project was very challenging. It really solidified my knowledge of how/when to pass variables back and fort between the .ejs and .js files. The logic there can be challenging for me, and this was a great opportunity to practice and become more fluent with making the web application run smoothly. I'm happy that this reinforced knowledge can be applied also to web development with Python/Flask.

## **_Angela Yu's Instructions for this Project:_**

#### **_Objectives:_**

-   Create a functioning Express/Node.js project which includes a PostgreSQL Database (create and accessed locally via pgAdmin 4).

-   Access and parse data from a remote API with JavaScript and asynchronous functions.

-   Deomonstrate fluency with JavaScript back and frontend development and Create/Read/Update/Delete data creation/manipulation both JavaScript database queries and using the pgAdmin query tool.

#### **_Requirements:_**

-   Database Persistance

-   Project Planning

-   Project Setup

-   API Integration

-   Data Presentation

-   Error Handling

-   Documentation

-   Code Sharing

#### **_How I Interpret the Instructions:_**

-   The suggested theme, which I utilize, is to incorporate book images into a list for reading suggestions in a creative, interesting way which the user could add to. THe OpenLibrary API is suggested, and I utilized a couple of its endpoints.

-   I create original HTML and CSS styling (and am happy with the result!), and compose all of the code from scratch, referring to my notes and researching any issues online, mainly at StackOverflow.

-   I generally try to avoid using ChatGPT, since I want to struggle as much as possible through the learning process to solidify my understanding independently, but when I got really stuck I did query this helpful tool. Once I complete the project I asked ChatGPT to look it over and make any suggestions, which I took to heart and learn from, and also to help with writing concise and incisive docstrings.

## **_My Steps in Completing this Project:_**

### **_1. Installing Node.js, PostgreSQL and pgAdmin, creating HTML/CSS Structure/Styling:_**

-   See above section **Requirements** for how I install the Node.js/Express packages.

-   The first step after intalling the required packages is designing an appealing structure/color/font schema for the website: see EJS and CSS files for the result.

-   Also I have fun designing a favicon in GIMP:

![favicon](public/images/faviconScreenshot.png)

### **_2. Setting up the Database in pdAdmin:_**

-   Create db `js_capstone_book`.

-   Use the Query Tool to:

```sql
CREATE TABLE book_recommendations (
    id SERIAL PRIMARY KEY,
	book_title VARCHAR(100) NOT NULL,
	book_author VARCHAR(100),
	book_url VARCHAR(100),
	book_recommender VARCHAR(100)
)
```

-   Add entries to get things started:

```sql
INSERT INTO book_recommendations (book_title, book_author, book_url, book_recommender)
VALUES ('Flight Path', 'Jan David Blais', 'https://covers.openlibrary.org/b/isbn/0965460703-L.jpg', 'Andrew'),
       ('Ubik', 'Philip K. Dick', 'https://covers.openlibrary.org/b/isbn/1857988531-L.jpg', 'Andrew'),
       ('The Elephant in the Brain', 'Kevin Simler & Robin Hanson', 'https://covers.openlibrary.org/b/isbn/0197551955-L.jpg', 'Andrew');
```

-   I increase the character allowance for the URL column:

```sql
ALTER TABLE book_recommendations
ALTER COLUMN book_url TYPE VARCHAR(150);
```

-   In pgAdmin, the table now appeare as:

![preliminary table view](public/images/db_view.jpg)

-   I later add columns for users to add comments, and to indicate when a book is added/updated. Here's the SQL code adding/altering the date columns, and the code adding the `book_comments` column to the database:

```sql
ALTER TABLE book_recommendations
ADD date_add VARCHAR(15);

ALTER TABLE book_recommendations
ADD date_update VARCHAR(15);

ALTER TABLE book_recommendations
RENAME COLUMN date_add to date_added;

ALTER TABLE book_recommendations
RENAME COLUMN date_update to date_updated;

ALTER TABLE book_recommendations
ADD book_comments VARCHAR(1000);
```

### **_3. Create the JavaScript:_**

-   The challenge is to smoothly access the database with JavaScript queries/commands.

-   In the main file `index.js` I built test all of the database functionality first by containing the book list data in an array. Once I got the HTML/EJS/CSS successfully integrate with `index.js`, I converted the functionality to access the pgAdmin database with proper queries. The array testing code is comment out in `index.js`

-   pgAdmin's Query Tool is quite helpful for testing SQL code before implementing it in JavaScript. The SQL to test inserting an entry:

```sql
INSERT INTO book_recommendations (book_title, book_author, book_url, book_recommender)
VALUES ('The Lord of the Rings', 'J.R.R. Tolkien', 'https://a.media-amazon.com/images/I/7125+5E40JL._SL1500_.jpg', 'Andrew')
```

-   The above pgAdmin query is the foundation from which I build the JavaScript:

```js
await db.query(
    `INSERT INTO book_recommendations
            (book_title,
            book_author,
            book_url,
            book_recommender,
            date_added,
            date_updated,
            book_comments)
        VALUES ($1, $2, $3, $4, $5, $6, $7)`,
    [
        resultBookData.title,
        resultBookData.author,
        imageURL,
        trimmedRecommender,
        dateAdded,
        dateAdded,
        trimmedBookComments,
    ]
);
```

-   I repeat the process, testing with the pgAdmin Query Tool and translating to JavaScript, with `DELETE` and `EDIT`.

### **_4. Sharing on GitHub:_**

-   I manually create the repository at [GitHub](https://github.com/), then use the following commands to get the ball rolling:

```bash
# Initialize a new Git repository in the current directory:
git init

# Add all files to the staging area, including respecting the .gitignore file:
git add --all

# Commit the staged files with a descriptive message:
git commit -m "first commit"

# Rename the current branch to `main` (common default branch name):
git branch -M main

# Add a remote repository with the name `origin` pointing to the specified GitHub URL:
git remote add origin https://github.com/andrewblais/jsCapstoneBook.git

# Push the `main` branch to the `origin` remote, and set `origin/main` as the upstream branch:
git push -u origin main
```

## **_Thoughts/Conclusions:_**

-   The toughest parts of this project

    -   Creating original, interesting and appealing styling with CSS/HTML/EJS.

    -   Setting up a Node.js project and making sure the directory/libraries are installed successfully.

    -   Passing information between the front and backends with constistent, clean and effective JavaScript and HTML naming conventions for variables/user input.

    -   Incorporating robust, manageable PostgreSQL queries with JavaScript.

-   The less challenging aspects of this project:

    -   Aside from the creative side of creating a Web Application, I'm very comfortable with HTML/CSS commands and options.

    -   Although the overall process of making this project was time-consuming, I felt in control and aware of all of the steps I needed to take. It was hard work, but I'm feeling much more fluent with JavaScript, Node.js, PostgreSQL and more advanced CSS conventions.

-   What to improve on in future projects:

    -   Consider making the CSS more compact. Although it's easier to read and maintain different tag/class properties when I repeat code for each element, in a larger web application it will become necessary to conserve resources.

    -   Don't get bogged down with details along the way. It's important to get work done without worrying about perfection. Be patient and know that subsequent drafts/refactoring is a part of the process.

    -   Consider the most effective approach to JavaScript, use functions intended to save code/processing time.

-   Overall, a fun, satisfying project, I'm happy with the work and learned a lot!

_Andrew Blais, September 1, 2024_

-   A screenshot of the Web Application:

![screenshot](public/images/webAppScreenshot.png)
