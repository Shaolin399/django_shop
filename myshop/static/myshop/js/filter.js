// filter.js

document.addEventListener('DOMContentLoaded', function() {
    const clearFiltersBtn = document.getElementById('clear-filters-btn');
    const minPriceInput = document.getElementById('min-price');
    const maxPriceInput = document.getElementById('max-price');
    const nfcCheckbox = document.getElementById('nfc-checkbox');
    const memorySelect = document.getElementById('memory');
    const brandSelect = document.getElementById('brand');
    const screenSizeSelect = document.getElementById('screen-size');
    const ramSelect = document.getElementById('ram');
    const batterySelect = document.getElementById('battery');
    const mainCameraSelect = document.getElementById('main-camera');
    const frontCameraSelect = document.getElementById('front-camera');
    const colorSelect = document.getElementById('color');
    const productGrid = document.querySelector('.product-grid');

    // Event listeners for filters
    clearFiltersBtn.addEventListener('click', function() {
        minPriceInput.value = '';
        maxPriceInput.value = '';
        nfcCheckbox.checked = false;
        memorySelect.value = '';
        brandSelect.value = '';
        screenSizeSelect.value = '';
        ramSelect.value = '';
        batterySelect.value = '';
        mainCameraSelect.value = '';
        frontCameraSelect.value = '';
        colorSelect.value = '';
        filterProducts();
    });

    // Add event listeners for other filters
    minPriceInput.addEventListener('change', filterProducts);
    maxPriceInput.addEventListener('change', filterProducts);
    nfcCheckbox.addEventListener('change', filterProducts);
    memorySelect.addEventListener('change', filterProducts);
    brandSelect.addEventListener('change', filterProducts);
    screenSizeSelect.addEventListener('change', filterProducts);
    ramSelect.addEventListener('change', filterProducts);
    batterySelect.addEventListener('change', filterProducts);
    mainCameraSelect.addEventListener('change', filterProducts);
    frontCameraSelect.addEventListener('change', filterProducts);
    colorSelect.addEventListener('change', filterProducts);

    // Initial filtering when page loads
    filterProducts();

    // Function to filter products based on selected filters
    function filterProducts() {
        // Logic to filter products based on selected criteria
        // Replace with your own logic to fetch and display products
        // Example: Fetch products via AJAX based on selected filters
        fetch('/api/products/?' + new URLSearchParams({
            min_price: minPriceInput.value,
            max_price: maxPriceInput.value,
            nfc: nfcCheckbox.checked,
            memory: memorySelect.value,
            brand: brandSelect.value,
            screen_size: screenSizeSelect.value,
            ram: ramSelect.value,
            battery: batterySelect.value,
            main_camera: mainCameraSelect.value,
            front_camera: frontCameraSelect.value,
            color: colorSelect.value
        })).then(response => response.json())
          .then(data => {
              // Update the product grid with filtered products
              productGrid.innerHTML = '';
              data.forEach(product => {
                  const productTile = document.createElement('div');
                  productTile.classList.add('product-tile');
                  productTile.innerHTML = `
                      <a href="/product/${product.id}">
                          <img src="${product.image_url}" alt="${product.name}">
                      </a>
                      <h3><a href="/product/${product.id}">${product.name}</a></h3>
                      <p class="price">${product.price} ₴</p>
                      <button class="add-to-cart-btn">Додати у корзину</button>
                  `;
                  productGrid.appendChild(productTile);
              });
          })
          .catch(error => {
              console.error('Error fetching products:', error);
          });
    }
});
