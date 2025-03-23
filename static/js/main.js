const dropDown = document.querySelector('.dropdown');
const avatar = document.querySelector('.avatar')
const messageBox = document.getElementById('message-box')
console.log(`message box: ${messageBox}`)
console.log("javascript")

// hide message after 5 seconds
setTimeout(function () {
    if (messageBox) {
        messageBox.style.display = 'none'
    }
}, 5000)

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

//create post modal
let modal = document.getElementById('modal')
let postBtn = document.getElementById('post-btn')
let closeBtn = document.querySelector('.close-btn')

postBtn.onclick = function() {
    modal.classList.remove('hidden')
}

closeBtn.onclick = function () {
    modal.classList.add('hidden')
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.classList.add('hidden')
    }
}
