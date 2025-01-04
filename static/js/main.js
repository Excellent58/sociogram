const dropDown = document.querySelector('.dropdown');
const avatar = document.querySelector('.avatar')

console.log(dropDown)
console.log(avatar)

// toggle dropdown
avatar.addEventListener('click', ()=> {
    if (dropDown.classList.contains('hidden')) {
        dropDown.classList.remove('hidden')
    } else {
        dropDown.classList.add('hidden')
    }
})


// dropdown click-away functionality
document.addEventListener('click', (event) => {
    if (!dropDown.classList.contains('hidden')) {
        if (!dropDown.contains(event.target) && !avatar.contains(event.target)) {
            dropDown.classList.add('hidden');
        }
    }
})