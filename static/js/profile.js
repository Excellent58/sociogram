let editModal = document.querySelector('.modal')
let editBtn = document.querySelector('.edit-btn')
let closeModalBtn = document.querySelector('.close-btn')
const messageBox = document.getElementById('message-box')

console.log("writing js")

editBtn.addEventListener('click', (event)=> {
    event.preventDefault()
    editModal.classList.remove('hidden')
})

closeModalBtn.addEventListener('click', ()=> {
    editModal.classList.add('hidden')
})

window.addEventListener('click', (event)=> {
    if (event.target === editModal) {
        editModal.classList.add('hidden')
    }
})


// hide message after 5 seconds
setTimeout(function () {
    if (messageBox) {
        console.log(messageBox)
        messageBox.style.display = 'none'
    }
}, 5000)