const navEl = document.querySelector('nav');

function changeColor(){
    navEl.addEventListener('click', function(){
        this.style.backgroundColor = '#fff';
    })
}

changeColor();