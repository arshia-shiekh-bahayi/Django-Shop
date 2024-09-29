function addToCart(product_id) {
  $.ajax({
      url: addToCartUrl,
      method: "POST",
      data: {
          product_id: product_id,
          csrfmiddlewaretoken: csrfToken
      },
      success: function (response) {
          console.log(response);
      },
      error: function (jqXHR, testStatus, errorThrown) {
          console.log(errorThrown);
      }
  });
}