function changePage(page_number) {
    let current_url_params = new URLSearchParams(window.location.search);
    current_url_params.set("page", page_number);
    let new_url = window.location.pathname + "?" + current_url_params.toString();
    window.location.href = new_url;
}


function formatPriceInToman(element) {
    // Get the raw price as a string and remove any non-digit characters (e.g., commas)
    let rawPriceString = element.innerText.replace(/[^\d]/g, '');
  
    // Convert the cleaned string to a floating-point number
    let rawPrice = parseFloat(rawPriceString);
  
    // Check if the parsed value is a valid number
    if (isNaN(rawPrice)) {
      console.error('Invalid price:', element.innerText);
      element.innerText = 'قیمت نامعتبر';
      return;
    }
  
    // Use Intl.NumberFormat to format the number in the Persian format
    let formatter = new Intl.NumberFormat('fa-IR');
    let formattedPrice = formatter.format(rawPrice);
  
    // Update the element's text with the formatted price in Toman
    element.innerText = `${formattedPrice} تومان`;
    
  }
  
  document.addEventListener("DOMContentLoaded", function () {
    let priceElements = document.querySelectorAll('.formatted-price');
    priceElements.forEach(element => formatPriceInToman(element));
  });
