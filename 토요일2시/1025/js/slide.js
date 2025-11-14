

const imgWrap=document.querySelector(".img-wrap");
const images=document.querySelectorAll(".img");

const slideWidth=1200;
const slideCount=images.length;

console.log("이미지개수:", slideCount)
function move(){
    imgWrap.style.marginLeft=`${-slideWidth}px`;
    const fitstLi=document.querySelector(".img:first-child");
    //const lastLi=document.querySelector(".img:last-child");

    imgWrap.insertBefore(fitstLi,null);
    imgWrap.style.marginLeft=0;

}

move()
