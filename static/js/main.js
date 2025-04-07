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

// const followUrl = "http://localhost:8000/accounts/follow"
const followForms = document.querySelectorAll('.follow-form')
followForms.forEach(form => {
    form.addEventListener('submit', async function(e) {
        e.preventDefault(); //prevent full page reload

        const followUrl = form.dataset.url; // <--- grab from data-url
        // console.log(`follow url: ${followUrl}`)
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
})

// bump animation after liking or unliking
const bumpAnimation = (el) => {
  el.classList.remove('scale-100');
  el.classList.add('scale-125');
  setTimeout(() => {
    el.classList.remove('scale-125');
    el.classList.add('scale-100');
  }, 200);
};

// like or unlike a post
document.querySelectorAll('.like-btn').forEach(button => {
    button.addEventListener('click', async (e) => {
        const postId = button.dataset.postId;
        const url = `/like-post/?post_id=${postId}`;

        const response = await fetch(url);
        const data = await response.json();

        if (response.ok) {
            const filled = button.querySelector('.heart-filled');
            const outline = button.querySelector('.heart-outline');

            filled.classList.toggle('hidden');
            outline.classList.toggle('hidden');

            bumpAnimation(filled);
            bumpAnimation(outline);
        } else {
            alert("failed to like/unlike post")
        }
        console.log(data)

        // const heartIcon = button.querySelector('.heart-icon');
        const countSpan = document.getElementById(`likes-count-${postId}`);

        // Update icon color
        // if (data.liked) {
        //     heartIcon.classList.remove('text-gray-400');
        //     heartIcon.classList.add('text-pink-500');
        // } else {
        //     heartIcon.classList.remove('text-pink-500');
        //     heartIcon.classList.add('text-gray-400');
        // }

        countSpan.textContent = data.likes_count;        
    }); 
});