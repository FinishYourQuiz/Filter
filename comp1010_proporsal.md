# *Replace with the title of your project*

## Contributors

Name: Ziyao Yang

Student number: z5183948

## Problem statement

###### *Give a brief description of the problem you are trying to solve. Don't include any technical details. Your description should be understandable to a reader with no technical background or domain knowledge.*

__Enhance the photo effect effectively, without any professional and tedious tools. Just click the name of effect you want then you will get the new photo.__

## Background

###### *Describe the context in which you are undertaking this project. You should include: any external resources on which your project depends (data sources, website APIs, Python libraries we've not covered in this course, etc.), existing solutions to the same or similar projects, and any other information that the reader needs to know to understand how you intend to solve the given problem.*
1. Sources:
    - FrontEnd : 
        - Languages: HTML, CSS, NodeJS
        - External Sources:
            - https://fonts.googleapis.com/icon?family=Material+Icons: For Icons uses.
    - BackEnd:
        - Language: Python (+ flask)
        - External Sources: 
            - PIL: Image Processing and some filters
            - uuid: To create unique strings
1. Existing solutions to the same or similar projects:
    - https://www.befunky.com/features/photo-effects/<br>
    - https://www.canva.com/photo-editor/

## Target users

###### *Who are the intended users of the application for which you are making a protoype? What are their needs? This section does not need to be long, but avoid being too broad in your description of the users. "Anyone who wants it" isn't a specific enough set of people to target an application.*

__Want to give their photo some effects__

## Minimum Viable Product/Prototype

###### *Consider what the simplest solution to the problem above would be. For this project, you are not required to produce a completely polished product fit for general use, but you should still take into account usability when deciding viability. In this section, describe a version of your application with the fewest possible features, but which would still be useful to the target users.*

1. ### A simple webpage which contains 
2. ### This webpage will use HTML+CSS+NodeJS for frontEnd, and Python(flask) in the background.
    1. #### __Basic Filters__: when clicked any following filter, the right-hand-side image will be sync by the effect.
        - Black and White
        - Old Film
        - Reverse: 255 - orginal image 
        - Red Enhance: Increase the red channel of image by certain paramaters.
        - Green Enhance: Increase the green channel of image.
        - Blue Enhance: Increase the blue channel of image.
        - Edge Enhance
        - Blur
        - Contour: Image contains the edges of the original image in black and white.
        - Detail: Increase the edges weights
        - Smooth: 
        - Sharpen: 
    1. #### __Image__:
        - When the URL changes, the image will be changed to the image provided by URL.
        - Size of image will be fitted to the window size.
        - When any effect is applied, there should be a Loading icon shows the process.
        - The defualt image should be displayed first.
    1. #### __Button can change the image url__:
        - Click the button, there should appear a input (for putting the url) and a button to comfirm change the url.
        - check the URL is valid  or not, if not valid throw an error.
        - If Valid, change the image url and update, close the input and button.
## Demonstration of feasibility

###### *Describe a core feature of your prototype application and provide a demonstration of how that feature may work in the code cell below (you can add further code cells if you wish). For example, if your application gets data from an external source, write code here that does that so you can demonstrate it is feasible. Similarly, if your application relies on you implementing an algorithm, using a library we haven't covered in the course, or generating images/visualisations, write code here does that.*



<br>


# "Nice to have" features

###### *Describe any additional features that would improve the experience of using your prototype for the target users. These features should not be strictly necessary for the prototype to be useful, but may include things most users would expect as standard. This could include things like: being able to register an account, saving user preferences, or social media integration. Features should be itemized with dot points or numbered.*

- More Filters
- Save Photo

## Stretch goals

###### *Include here any features that would make your prototype really shine, but which you are not confident you can implement in the time available for this project. Don't be afraid to be ambitious in selecting stretch goals. See the marking scheme for the final prototype for information on what marks are available for completing stretch goals. Stretch goals should be itemized with dot points or numbered.*

- UI/UX Effects

## Marking Criteria

The table below contains the marking criteria for this proposal. Don't delete it as your tutor will fill it in during marking.

| Criteria | Mark | Notes | 
| -------------------------------------------------------- | ---- | --- |
| Clearly defined problem to be solved (1 mark)                                     |      | |
| Background includes information necessary for building a prototype (2 mark)       |      | |
| Appropriate set of target users (1 marks)                                         |      | |
| MVP is both minimal and viable (1 marks)                                          |      | |
| Code in feasibility demonstration produces an appropriate result (3 marks)        |      | |
| Comprehensive list of "nice to have" features (1 mark)                            |      | |
| Appropriate ambitious stretch goals (1 mark)                                      |      | |
