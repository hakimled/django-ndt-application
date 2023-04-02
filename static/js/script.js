

function changeColor(){
    const navEl = document.querySelector('header');
    navEl.addEventListener('click', function(){
        this.style.backgroundColor = '#fff';
    })
}

changeColor();