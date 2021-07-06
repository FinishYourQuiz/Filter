new_image = "file:///Users/ssss/Desktop/COMP%201010/Project/sample.jpeg"

function getNewPhoto(){
    // console.log(document.getElementById("new_image").src)
    fetch('http://127.0.0.1:5000/test', {
        body: JSON.stringify({
            mode: 'no-cors',
            credentials: 'include',
            'image': '/Users/ssss/Desktop/COMP 1010/Project/sample.jpeg',
        }),
        headers: {
            'content-type': 'application/json',
        },
        method: 'POST',
    })
}