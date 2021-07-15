import isImageUrl from 'node_modules/is-image-url';

const getNewPhoto = (ROUTE) => {
    document.getElementById('Wait').hidden = false;
    console.log(document.getElementById("new_image").src);
    fetch("http://localhost:8000/"+ROUTE, {
        body: JSON.stringify({
            mode: 'no-cors',
            credentials: 'include',
            'image': document.getElementById('raw_image').src,
        }),
        headers: {
            'content-type': 'application/json',
        },
        method: 'POST',
    }).then( res => {
        return res.json();
    }).then( res => {
        document.getElementById("new_image").src = '';
        document.getElementById("new_image").src = res['new_image'];
        document.getElementById('Wait').hidden = true;
    })
} 

const display = () => {
    if(document.getElementById('url').hidden){
        document.getElementById('url').hidden = false;
    }else{
        document.getElementById('url').hidden = true;
    }
}

function updateURL(){
    var url = document.getElementById('image_url').value;
    if(isImageUrl(url)){
        document.getElementById('raw_image').src = url;
        document.getElementById('new_image').src = url;
        document.getElementById('url').hidden = true;
        console.log(document.getElementById('image_url').src);
        console.log(document.getElementById('raw_image').src);
    }else{
        console.log('Invalid URL!')
    }
}