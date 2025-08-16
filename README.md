# crowdfunding_backend
Django_Project

# Crowdfunding Back End
{{ your name here }}

## Planning:
### Concept/Name
{{ Include a short description of your website concept here. }}

### Intended Audience/User Stories
{{ Who are your intended audience? How will they use the website? }}

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


### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )
![](./database.drawio.svg)