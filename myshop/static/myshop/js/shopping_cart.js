//shoping_cart.js
document.addEventListener('DOMContentLoaded', () => {
    const cartItemsContainer = document.getElementById('cart-items');
    const cartTotalElement = document.getElementById('cart-total');
    
    // Функція для відображення товарів у кошику
    const displayCartItems = () => {
        const cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
        cartItemsContainer.innerHTML = '';
        let total = 0;

        cartItems.forEach((item, index) => {
            const cartItem = document.createElement('div');
            cartItem.className = 'cart-item';
            cartItem.innerHTML = `
                <img src="${item.img}" alt="${item.name}">
                <div>
                    <h3>${item.name}</h3>
                    <p class="price">${item.price} ₴</p>
                    <button class="remove-from-cart" data-index="${index}">Видалити</button>
                </div>
            `;
            cartItemsContainer.appendChild(cartItem);
            total += item.price;
        });

        cartTotalElement.innerText = `${total} ₴`;

        // Додаємо обробник подій для кнопок "Видалити"
        const removeFromCartButtons = document.querySelectorAll('.remove-from-cart');
        removeFromCartButtons.forEach(button => {
            button.addEventListener('click', (e) => {
                const index = e.target.dataset.index;
                removeFromCart(index);
            });
        });
    };

    // Функція для видалення товару з кошика
    const removeFromCart = (index) => {
        let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
        cartItems.splice(index, 1);
        localStorage.setItem('cartItems', JSON.stringify(cartItems));
        displayCartItems();
    };

    displayCartItems();
});
