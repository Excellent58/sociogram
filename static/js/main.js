const dropDownSection = document.querySelector(".dropdown-sec")
const dropDown = document.querySelector(".dropdown")

dropDownSection.addEventListener("click", function () {
    if(dropDown.classList.contains('hidden')) {
        dropDown.classList.remove('hidden');
    } else {
        dropDown.classList.add('hidden');
    }
})