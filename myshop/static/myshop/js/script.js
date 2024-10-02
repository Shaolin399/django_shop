// script.js

document.addEventListener('DOMContentLoaded', function() {
    const productsContainer = document.querySelector('.product-grid');
    const products = Array.from(productsContainer.children);

    const filterProducts = () => {
        const minPrice = parseInt(document.getElementById('min-price').value) || 0;
        const maxPrice = parseInt(document.getElementById('max-price').value) || Infinity;
        const memory = document.getElementById('memory').value;
        const brand = document.getElementById('brand').value;
        const battery = document.getElementById('battery').value;
        const cameraResolution = document.getElementById('camera-resolution').value;

        products.forEach(product => {
            const productPrice = parseInt(product.dataset.price);
            const productMemory = product.dataset.memory;
            const productBrand = product.dataset.brand;
            const productBattery = product.dataset.battery_capacity;
            const productResolution = product.dataset.camera_resolution;

            const isVisible = productPrice >= minPrice &&
                              productPrice <= maxPrice &&
                              (memory === '' || productMemory === memory) &&
                              (brand === '' || productBrand === brand) &&
                              (battery === '' || productBattery === battery) &&
                              (cameraResolution === '' || productResolution === cameraResolution);

            product.style.display = isVisible ? '' : 'none';
        });
    };

    // Event listeners for filters
    document.getElementById('min-price').addEventListener('input', filterProducts);
    document.getElementById('max-price').addEventListener('input', filterProducts);
    document.getElementById('memory').addEventListener('change', filterProducts);
    document.getElementById('brand').addEventListener('change', filterProducts);
    document.getElementById('battery').addEventListener('change', filterProducts);
    document.getElementById('camera-resolution').addEventListener('change', filterProducts);

    // Clear filters button
    document.getElementById('clear-filters-btn').addEventListener('click', function() {
        document.getElementById('min-price').value = '';
        document.getElementById('max-price').value = '';
        document.getElementById('memory').value = '';
        document.getElementById('brand').value = '';
        document.getElementById('battery').value = '';
        document.getElementById('camera-resolution').value = '';
        filterProducts();
    });

    // Fetch filter options from Django view
    fetch('/filter-options/')
        .then(response => response.json())
        .then(data => {
            const { brands, memories, batteries, cameraResolutions } = data;

            const memorySelect = document.getElementById('memory');
            memories.forEach(memory => {
                memorySelect.innerHTML += `<option value="${memory}">${memory} ГБ</option>`;
            });

            const brandSelect = document.getElementById('brand');
            brands.forEach(brand => {
                brandSelect.innerHTML += `<option value="${brand}">${brand}</option>`;
            });

            const batterySelect = document.getElementById('battery');
            batteries.forEach(battery => {
                batterySelect.innerHTML += `<option value="${battery}">${battery} мАг</option>`;
            });

            const cameraResolutionSelect = document.getElementById('camera-resolution');
            cameraResolutions.forEach(resolution => {
                cameraResolutionSelect.innerHTML += `<option value="${resolution}">${resolution} Мп</option>`;
            });

            filterProducts(); // Filter products initially based on default selections
        })
        .catch(error => {
            console.error('Error fetching filter options:', error);
        });
});
