let thumbnails = document.getElementsByClassName('thumbnail');
let slider = document.getElementById('slider');

let buttonRight = document.getElementById('slide-right');
let buttonLeft = document.getElementById('slide-left');

buttonLeft.addEventListener('click', function(){
    slider.scrollLeft -= 125;
})
buttonRight.addEventListener('click', function(){
    slider.scrollLeft += 125;
})
const maxScrollLeft = slider.scrollWidth - slider.clientWidth; 
function autoPlay() {
    if (slider.scrollLeft > (maxScrollLeft - 1)) {
        slider.scrollLeft -= maxScrollLeft;
    } else {
        slider.scrollLeft += 1;
    }
}
let play = setInterval(autoPlay, 50);
for (var i=0; i < thumbnails.length; i++){
thumbnails[i].addEventListener('mouseover', function() {
    clearInterval(play);
});

thumbnails[i].addEventListener('mouseout', function() {
    return play = setInterval(autoPlay, 50);
});
}

function videourl(hm){
    var video =document.getElementById("videoslider");
    video.src=hm;
    if(video.muted){
        video.muted=false;
    }
    
}
function photourl(hm){
    var photo =document.getElementById("photoslider");
    photo.src=hm;    
}