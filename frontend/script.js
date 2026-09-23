function openTask() {
    let modal = document.getElementById("taskModal");

    if (modal) {
        modal.style.display = "flex";
    }
}


function closeTask() {
    let modal = document.getElementById("taskModal");

    if (modal) {
        modal.style.display = "none";
    }
}


window.onclick = function(event) {

    let modal = document.getElementById("taskModal");

    if (event.target === modal) {
        modal.style.display = "none";
    }

};