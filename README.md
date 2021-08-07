## __Contributor__
$$\bold{Name: Ziyao\ Yang}$$

$$\bold{Student\ number:  z5183948}$$

## __Problem statement__

__Enhance the photo effect effectively, without using any professional or tedious tool. Just select the filter then you will get the new photo you want to see.__ 

## __Status__

| Category      | Feature                                                                                                         | Status    |
| ------------- | --------------------------------------------------------------------------------------------------------------- | --------- |
| __MVP__           | User can enter any URL of an image for later adding effect.                                                     | __Completed__ |
| __MVP__           | A menu of filters should be shown in the page                                                                   | __Completed__ |
| __MVP__           | User can see displayed image after they comfirm the url of new image.                                           | __Completed__ |
| __MVP__           | The filtered image should be displayed when user clicks/chooses filter                                          | __Completed__ |
| __MVP__           | 'Black and White' filter should be displayed the correct effect.                                                | __Completed__ |
| __Nice to Have__  | More Filters: Reverse, Old Film (Vintage), Blur, Contour, Edge Enhance, Sharpen.                                | __Completed__ |
| __Nice to Have__  | When any effect is applied, there should be a Loading icon before the frontend gets the new image from backend. | __Completed__ |
| __Nice to Have__  | User can see a defualt image and choose replace the image by a new URL or keep continue on the defualt image.   | __Completed__ |
| __Nice to Have__  | User can save the image                                                                                         | __Attampted__ |
| __Nice to Have__  | Click the button, there should appear a input (for putting the url) and a button to comfirm change the url.     | __Completed__ |
| __Nice to Have__  | User cannot input an invalid URL, if an useless URL inputed, an error should be displayed.                      | __Completed__ |
| __Stretch Goals__ | More filters: Blur effects, edge effect, color effects                                                          | __Completed__ |
| __Stretch Goals__ | Users are able to crop, resize or rotate the image.                                                             | __Completed__ |
| __Stretch Goals__ | User can add a frame outside the image.                                                                         | __Completed__ |
| __Stretch Goals__ | The filters can be classified correctly and shown in different menu                                             | __Completed__ |
| __Stretch Goals__ | User can select the level of enhance, like low, medium or high.                                                 | __Completed__ |
| __Stretch Goals__ | After user close the webpage, user can see the latest change on the image next time.                            |           |

## __To Run This Project__
    # pip install 
    Flask==2.0.1
    Flask-Cors==3.0.10
    numpy==1.21.1
    Pillow==8.3.1

    # Or just simply:     
    pip install -r requirements.text

    # Then run:
    flask run

    # And open 'main.html'