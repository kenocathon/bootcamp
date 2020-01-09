

function moveBoxSlow(){
    var box = document.getElementById('square');
    box.classList.add('moveBoxSlow');
    const animated = document.querySelector('.moveBoxSlow')
    animated.addEventListener('animationend', () =>{
    box.classList.remove('moveBoxSlow');
    });
    
}
function moveBoxFaster(){
    var box = document.getElementById('square')
    box.classList.add('moveBoxFaster');
    const animated = document.querySelector('.moveBoxFaster')
    animated.addEventListener('animationend', () =>{
    box.classList.remove('moveBoxFaster');
    });
}
function moveBoxFastest(){
    var box = document.getElementById('square')
    box.classList.add('moveBoxFastest');
    const animated = document.querySelector('.moveBoxFastest')
    animated.addEventListener('animationend', () =>{
    box.classList.remove('moveBoxFastest');
    });
}



