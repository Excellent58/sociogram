let editModal = document.querySelector('.modal')
let editBtn = document.querySelector('.edit-btn')
let closeModalBtn = document.querySelector('.close-btn')

editBtn.addEventListener('click', ()=> {
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