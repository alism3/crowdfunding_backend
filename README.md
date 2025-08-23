# crowdfunding_backend
Django_Project

# Crowdfunding Back End
{{ your name here }}

## Planning:
### Concept/Name
Alpaca Paws & Causes: A whimsical crowdfunding platform dedicated to supporting alpaca farms 
and the adorable alpacas themselves. The idea is to offer unique, humor-filled "pledge levels" 
that connect donors directly to the specific needs and quirky personalities of the 
alpaca community. From funding "Marta's Shopping Spree" (for a new Prada bag, of course!) 
to ensuring "Mama Alpaca's Brood" is well-fed or buying "Christmas Sweaters for 
Shearling Alpacas," we make giving fun and impactful. 
My goal is to bring a smile to your face while providing vital support to alpaca 
farmers and their fluffy friends.

### Intended Audience/User Stories
{{ Who are your intended audience? How will they use the website? }}
AUDIENCE
- Animal lovers, especially those with a fondness for alpacas. (Like Me)
- People looking for unique and humorous gift ideas. (Can be part of a gift for a birthday, your friends make a donation and you receive a personalize photo of an Alpaca)
- Individuals interested in supporting small, sustainable farming initiatives.
- People who enjoy engaging with community-driven projects.
- Existing fans or visitors of alpaca farms who want to offer direct support.

USER STORIES
As a potential donor:
  -  I want to easily browse different alpaca fundraising campaigns so I can find one that resonates with me. (e.g., I want to help Marta with her Prada addiction.)
  - I want to see different humorous pledge levels with clear descriptions so I can choose how much I want to contribute and what "cause" I'm supporting. (e.g., I want to donate to the "Christmas Sweater" fund.)
  - I want to securely make a pledge so my contribution reaches the farmer.
  - I want to receive updates on the campaign I supported so I can see the impact of my donation. (e.g., Did Marta get her bag? Are the alpacas warm?)
As an alpaca farmer, 
  - I want to create a new fundraising campaign with unique and funny pledge categories so I can effectively raise funds for my specific needs. (e.g., I need money for new fencing, but I'll make it sound like the alpacas are escaping to find better snacks.)
  - I want to track the progress of my campaigns and see who has pledged so I can manage my fundraising efforts.
  -  I want to be able to post updates to my campaign so I can keep donors engaged and informed.

### Front End Pages/Functionality
- Home page
    - Featured fundraiser
-   Search page
      - 
     {{ A list of dot-points showing functionality is available on this page }}
    - {{ etc }}
    - {{ etc }}
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}

Home page
	- Featured fundraiser (e.g., "This Month's Funniest Cause: Alpacas Against Bland Hay!")
	- Recently added or trending campaigns.
	- Call to action for new farmers to create a campaign.
	- Search bar for finding specific campaigns.
	- About Us/How it Works section.
  
Search/Browse Campaigns Page
	- List of all active fundraising campaigns, with short descriptions and progress bars.
	- Filtering options (e.g., by category: "Aesthetic," "Social Help," "Alpaca Comfort").
	- Sorting options (e.g., by amount raised, newness, ending soon).
	- Pagination for a large number of campaigns.
  
Single Campaign Detail Page
	- Full description of the campaign and the farmer.
	- Detailed progress bar and target amount.
	- List of unique, humorous pledge levels with descriptions and associated donation amounts.
	- Button to "Make a Pledge."
	- Section for campaign updates (from the farmer).
	- Comments/discussion section (optional).
	- Share buttons (social media).

User Dashboard/Profile Page 
for logged-in users
	- List of campaigns the user has pledged to.
	- Ability to view pledge history.
For farmers
    - List of their active and past campaigns.
	- Option to create a new campaign.
	- Ability to edit/update their campaigns.

Pledge Confirmation/Payment Page
	- Summary of the chosen pledge level and amount.
	- Secure payment gateway integration.
	- Confirmation of successful pledge.

Create/Edit Campaign Page (for farmers)
	- Form fields for campaign title, description, target amount, end date.
	- Ability to define multiple pledge levels with descriptions and amounts.
	- Option to upload images/videos for the campaign.
	- Preview function.
  
Login/Registration Page
	- Standard user authentication.

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL             | HTTP Method | Purpose                    | Request Body | Success Response Code | Authentication/Authorisation |
| --------------- | ----------- | -------------------------------- | ------------ | --------------------- | ---------------------------- |
| /fundraisers/   | GET         | Fetch all the fundraisers        | N/A          | 200                   | None                         |
| /fundraisers/   | POST        | Create a new fundraiser          | JSON Payload | 201                   | Any logged in user           |
| /fundraisers/1/ | GET         | Fetch a single fundraiser by ID  | N/A          | 200                   | None                         |
| /pledges/       | GET         | Fetch all pledges                | N/A          | 200                   | (?)                          |
| /pledges/       | POST        | New pledges for a fundraiser     | JSON payload | 201                   | Any logged in user           |
| /pledges/       | POST        | New pledges for a fundraiser     | JSON payload | 201                   | Any logged in user           |



### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )
![](./database.drawio.cdsvg)