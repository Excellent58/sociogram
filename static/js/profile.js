let editModal = document.querySelector('.modal')
let editBtn = document.querySelector('.edit-btn')
let closeModalBtn = document.querySelector('.close-btn')
const messageBox = document.getElementById('message-box')

if (editBtn) {
    editBtn.addEventListener('click', (event)=> {
    event.preventDefault()
    editModal.classList.remove('hidden')
})
}


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

const form = document.querySelector('.follow-form')

form.addEventListener('submit', async function(e) {
    e.preventDefault(); //prevent full page reload

    const followUrl = form.dataset.url; // <--- grab from data-url
    console.log(`follow url: ${followUrl}`)
    const formData = new FormData(form);
    const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;

    const response = await fetch(followUrl, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
        },
        body: formData
    });

    const data = await response.json();
    const button = form.querySelector('.follow-btn');
    button.textContent = data.is_following ? 'Following' : 'Follow';
});