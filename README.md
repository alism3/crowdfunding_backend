# Crowdfunding Back End
Alpaca_Heaven

# Link to the Deployed Project
https://alpaca-heaven-69a960f4f662.herokuapp.com/

## Planning:
### Concept/Name
A crowdfunding platform dedicated to supporting alpaca farms and the adorable alpacas themselves. The idea is to offer unique, humor-filled "pledge levels" that connect donors directly to the specific needs and quirky personalities of the 
alpaca community. From funding "Marta's Shopping Spree" (for a new Prada bag, of course!) 
to ensuring "Mama Alpaca's Brood" is well-fed or buying "Christmas Sweaters for 
Shearling Alpacas". The idea is to make giving fun and impactful. 
My goal is to bring a smile to your face while providing vital support to alpaca farmers and their fluffy friends.

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
  - I want to easily browse different alpaca fundraising campaigns so I can find one that resonates with me. (e.g., I want to help Marta with her Prada addiction.)
  - I want to see different humorous pledge levels with clear descriptions so I can choose how much I want to contribute and what "cause" I'm supporting. (e.g., I want to donate to the "Christmas Sweater" fund.)
  - I want to securely make a pledge so my contribution reaches the farmer.
  
As an alpaca farmer:
  - I want to create a new fundraising campaign with unique and funny pledge categories so I can effectively raise funds for my specific needs. (e.g., I need money for new fencing, but I'll make it sound like the alpacas are escaping to find better snacks.)
  - I want to track the progress of my campaigns and see who has pledged so I can manage my fundraising efforts.
  - I want to be able to post updates to my campaign so I can keep donors engaged and informed.

### Front End Pages/Functionality
-   Home Page: Displays all active fundraisers, calls to action for new farmers.
-   Single Campaign Detail Page: Full description of a campaign, "Make a Pledge" button, campaign updates, share options.
-   User Dashboard/Profile Page (for logged-in users)**:
		Supporter only: List of pledged campaigns, pledge history.
		Farmers only: List of active campaigns, options to create/edit/update campaigns.
-   Pledge Confirmation/Payment Page: Summary, confirmation.
-   Create/Edit Campaign Page (for farmers): Form fields for campaign details, pledge levels, image/video uploads, preview.
-   Login/Registration Page: Standard user authentication.

## Features

User Authentication & Authorization: 
     - Secure user registration 
     - Login (using token-based authentication)
     - Permission management (owners and supporters).
Fundraiser Management:
     - Create, view, update, and retrieve fundraiser campaigns.
     - A list of information for each fundraiser
     - Track of the total amount pledged for each fundraiser.
Pledge System:
     - Users can make pledges to fundraisers, specifying an amount, comment, and anonymity status.
     - Pledges are linked to fundraisers and individual supporters.
Permissions: 
     - Only owners can edit their own content
     - Only supporters can manage their pledges.

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL                | HTTP Method | Purpose                               | Request Body | Success Response Code | Authentication/Authorisation |
| ---------------    | ----------- | --------------------------------      | ------------ | --------------------- | ---------------------------- |
| /fundraisers/      | GET         | Fetch all the fundraisers             | N/A          | 200                   | None                         |
| /fundraisers/      | POST        | Create a new fundraiser               | JSON Payload | 201                   | Any logged in user           |
| /fundraisers/<pk>/ | GET         | Fetch a single fundraiser by ID       | N/A          | 200                   | None                         |
| /fundraisers/<pk>/ | PUT         | Update a single fundraisers by ID     | JSON Payload | 200                   | Any logged in user           |
| /pledges/          | GET         | Fetch all the pledges                 | N/A          | 200                   | None                         |
| /pledges/          | POST        | Create a new pledges for a fundraiser | JSON payload | 201                   | Any logged in user           |
| /pledges/<pk>/     | GET         | Fetch a single pledge by ID           | N/A          | 200                   | None                         |
| /pledges/<pk>/     | PUT         | Update a single pledge by ID          | JSON Payload | 200                   | Any logged in user           |
| /users/            | GET         | Fetch all the users                   | N/A          | 200                   | None                         |
| /users/            | POST        | Register a new user                   | JSON payload | 201                   | Any logged in user           |
| /api-token-auth/   | POST        | Obtain an authentication token        | JSON Payload | 200                   | None                         |


# Evidence of a successful method for each endpoint

GET METHOD
  - Get (Fetch all the fundraisers)
		C:\Users\alice\Desktop\SheCodesAU\crowdfunding_backend\Screenshoot_Insomnia\Get_all_Fundraisers.png
  - Get (Fetch all the pledges)
		C:\Users\alice\Desktop\SheCodesAU\crowdfunding_backend\Screenshoot_Insomnia\Get_all_Pledges.png
  - Get (Fetch all the users)
		C:\Users\alice\Desktop\SheCodesAU\crowdfunding_backend\Screenshoot_Insomnia\Get_all_users.png
 - Get (Fetch a single fundraiser by ID)
		C:\Users\alice\Desktop\SheCodesAU\crowdfunding_backend\Screenshoot_Insomnia\Get_FundbyID.png
  - Get (Fetch a single pledge by ID)
		C:\Users\alice\Desktop\SheCodesAU\crowdfunding_backend\Screenshoot_Insomnia\Get_PledbyID.png
  - Get (Obtain an authentication token)
		C:\Users\alice\Desktop\SheCodesAU\crowdfunding_backend\Screenshoot_Insomnia\Get_users_token.png

POST METHOD
  - Post (Create a new fundraiser)
		C:\Users\alice\Desktop\SheCodesAU\crowdfunding_backend\Screenshoot_Insomnia\Post_Create_NewFund.png
  - Post (Create a new pledge)
		C:\Users\alice\Desktop\SheCodesAU\crowdfunding_backend\Screenshoot_Insomnia\Post_Create_NewPledge.png
  - Post (Create a new user)
		C:\Users\alice\Desktop\SheCodesAU\crowdfunding_backend\Screenshoot_Insomnia\Post_Create_Newuser.png

PUT METHOD
  - Put (Update a single fundraisers by ID)
		Before ---> C:\Users\alice\Desktop\SheCodesAU\crowdfunding_backend\Screenshoot_Insomnia\Put_UpdateFundGoal.png
		After ----> C:\Users\alice\Desktop\SheCodesAU\crowdfunding_backend\Screenshoot_Insomnia\Put_UpdateFundGoal2.png
  - Put (Update a single pledge by ID)
		Before ---> C:\Users\alice\Desktop\SheCodesAU\crowdfunding_backend\Screenshoot_Insomnia\Put_UpdatePledGoal.png
		After ----> C:\Users\alice\Desktop\SheCodesAU\crowdfunding_backend\Screenshoot_Insomnia\Put_UpdatePledGoal2.png

## Step by Step to create a new user:
1. To create a new user, I need to send a POST request to the '/users/' endpoint
   - Open Insomnia and click on "Create a new user" in my "User" folder, link is https://alpaca-heaven-69a960f4f662.herokuapp.com/users/
   - Open the section "Body" and write in Json format username, email and password
   - Send the request, if successful I will have the confirmation about my new user (example: C:\Users\alice\Desktop\SheCodesAU\crowdfunding_backend\Screenshoot_Insomnia\Post_Create_Newuser.png)
2. To prove that I am who I am as a user, I need to Obtain the Authorization Token (for the Log In). To do this I have to send a POST request to the /api-token-auth/ endpoint
   - On Insomnia click on "Get user Token (Patricia)" in my "User" folder, link is https://alpaca-heaven-69a960f4f662.herokuapp.com/api-token-auth/
   - Put in the body the "username" and "password" to get the token (example: C:\Users\alice\Desktop\SheCodesAU\crowdfunding_backend\Screenshoot_Insomnia\Post_Create_Newuser.png)
   - Send the request, If successful, your terminal will show a JSON response with your unique authentication token
3. With the token, it's possible to create a new fundraiser because I need to be authenticated to complete this request and now I need to I need to send a POST request to the '/users/' endpoint
   - On Insomnia click on "Create a new fundraiser" in my "Fundraisers" folder, link is https://alpaca-heaven-69a960f4f662.herokuapp.com/fundraisers/
   - Put the details about the fundraiser (title, description, goal, image URL, and if it's open).
   - In the section "Prefix" write "Token " (Capital letter and space at the end is important) 
   - In the section "Auth", in the field "Body" write $response and select "response => body attribute", cancel the $ and click on the red rectangle to open other options.
   - In the field "Request" I selected the right Token that I used before to get the token (in my case "Get Auth Token (Patricia)"), in the "filter" fiels put "$.token" and the correct token should appear and click on "done" (example: C:\Users\alice\Desktop\SheCodesAU\crowdfunding_backend\Screenshoot_Insomnia\Get_users_token.png)
   - Send the request, If successful, the terminal will show a JSON response confirming your fundraiser was created. I would also be able to see it when I try to "Fetch all of fundraisers"


### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )
![](./database.drawio.svg)

Below is the conceptual database schema for the Alpaca Heaven backend.
Path: C:\Users\alice\Desktop\SheCodesAU\crowdfunding_backend\database.drawio.svg
![](./database.drawio.svg)
