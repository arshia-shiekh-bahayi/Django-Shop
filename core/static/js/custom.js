function changePage(page_number) {
    console.log("Custom.js is loaded");
    let current_url_params = new URLSearchParams(window.location.search);
    current_url_params.set("page", page_number);
    let new_url = window.location.pathname + "?" + current_url_params.toString();
    window.location.href = new_url;
}


function formatPriceInToman(element) {
    console.log("Custom.js is loaded");
    let rawPrice = parseFloat(element.innerText);
    let formatter = new Intl.NumberFormat('fa-IR');
    let formattedPrice = formatter.format(rawPrice);
    element.innerText = `${formattedPrice} تومان`;
}

window.onload = function() {
    console.log("Custom.js is loaded");
    let priceElements = document.querySelectorAll('.formatted-price');
    priceElements.forEach(element => formatPriceInToman(element));
};