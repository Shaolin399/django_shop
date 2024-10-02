//product_script.js
document.addEventListener('DOMContentLoaded', function() {
    // Отримуємо дані товару з localStorage
    const productData = JSON.parse(localStorage.getItem('productData'));

    // Отримуємо елементи, які ми будемо маніпулювати
    const productImageElement = document.querySelector('.product-details img');
    const productNameElement = document.querySelector('.product-details h1');
    const productPriceElement = document.querySelector('.product-details .price');

    // Встановлюємо текст для заголовка товару і ціни, а також src і alt для зображення
    productImageElement.src = productData.imageSrc;
    productImageElement.alt = productData.imageAlt;
    productNameElement.textContent = productData.name;
    productPriceElement.textContent = productData.price;
});
