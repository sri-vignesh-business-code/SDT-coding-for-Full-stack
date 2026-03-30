function showToast(message) {
    let toast = document.getElementById("toast");
    toast.innerHTML = message;
    toast.style.display = "block";

    setTimeout(() => {
        toast.style.display = "none";
    }, 4000);
}

function checkLowStock() {
    fetch('/low_stock')
    .then(res => res.json())
    .then(data => {
        if (data.length > 0) {
            let names = data.map(m => m.name).join(", ");
            showToast("⚠ Low Stock: " + names);
        }
    });
}

setInterval(checkLowStock, 8000);