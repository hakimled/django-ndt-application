

function changeColor(){
    const navEl = document.querySelector('header');
    navEl.addEventListener('click', function(){
        this.style.backgroundColor = '#444444';
        console.log('hi');
    })
}

changeColor();