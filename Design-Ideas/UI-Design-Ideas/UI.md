# Create a New Project Page

![enter image description here](https://raw.githubusercontent.com/jainal09/CrawlerX/design/Design-Ideas/UI-Design-Ideas/Create%20Project.png)

## Description:

In this section, all users can create a new project in the CrawlerX web app. Projects are like repositories in GitHub which allows users to organize and add multiple jobs or batches of crawling jobs.
In the project creation page, users must add details such as:
1. Project Name

2. Scrape From - Tor and https (both can also be selected)

3. Url list - Can be added manually or they can upload a .txt file of URLs

4. Select the data which they want to Scrap :
- Can select predefined options such as Emails, dates, bitcoin address ....
- Or can enter custom inputs such as search keywords, regex patterns, or specific div tags to scrap.

5.  Also, I have added an option to run as a cron job. If a user wants to scrap websites every day or a specific day automatically, they can select the date or time to run the job.

# Project Page

![enter image description here](https://raw.githubusercontent.com/jainal09/CrawlerX/design/Design-Ideas/UI-Design-Ideas/Project%20View.png)

## Description:

In this section, the user can see the ongoing crawling jobs
with the status of jobs.
1. ***Pending*** :
Crawling is in progress and not completed. (celery task is on-going)

2. ***Finished*** :
Crawling is completed and the result is saved in MongoDB.

3. ***Failed*** :
The Crawling tasks failed due to network-related issues, or website-down issues and the crawling job failed. (celery task failed and the detailed log is created)

There are also options for filtering websites and sorting the website list based on date, time or status.

Also, have a look at the left navigation drawer. With the help of that one can quickly browse all the created projects in one click.

# Search Page

![enter image description here](https://raw.githubusercontent.com/jainal09/CrawlerX/design/Design-Ideas/UI-Design-Ideas/Search%20View.png)

## Description:

● The Search page is self-explanatory – it is where users can search crawled results from the database.

● The search bar is a fuzzy search bar having auto suggestion features like google search.

● Additionally, here the data is being searched in a very predictive and accurate manner through elastic search (more details are explained in the backend implementation section).
