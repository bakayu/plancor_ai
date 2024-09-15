const cartSidebar = document.querySelector('.cart-sidebar');
const cartItemsList = document.querySelector('#cart-items');
const closeCartButton = document.querySelector('#close-cart');
const cartLink = document.querySelector('#cart-link');
const cartCountSpan = document.querySelector('#cart-count');

let cart = [];

document.addEventListener('DOMContentLoaded', () => {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    addToCartButtons.forEach((button) => {
        button.addEventListener('click', (e) => {
            const productId = e.target.dataset.productId;
            const productItem = e.target.parentNode;
            const productName = productItem.querySelector('h3').textContent;
            const productPrice = productItem.querySelector('p').textContent;

            cart.push({ id: productId, name: productName, price: productPrice });
            updateCartCount();

            cartSidebar.classList.add('show');
            renderCartItems();
        });
    });

    closeCartButton.addEventListener('click', () => {
        cartSidebar.classList.remove('show');
    });
    

    cartLink.addEventListener('click', (e) => {
        e.preventDefault();
        cartSidebar.classList.toggle('show');
    });
});


function updateCartCount() {
    cartCountSpan.textContent = cart.length;
}
function renderCartItems() {
    cartItemsList.innerHTML = '';
    cart.forEach((item) => {
        const cartItemHTML = `
            <li>
                <span>${item.name}</span>
                <span>${item.price}</span>
            </li>
        `;
        cartItemsList.innerHTML += cartItemHTML;
    });
}

const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');
const sliderInner = document.querySelector('.product-slider-inner');
const slides = document.querySelectorAll('.product-item');
const slideWidth = slides[0].offsetWidth;
let slideIndex = 0;

// Clone all slides and append them to the end of the slider
slides.forEach((slide) => {
  const slideClone = slide.cloneNode(true);
  sliderInner.appendChild(slideClone);
});

prevBtn.addEventListener('click', () => {
  slideIndex = (slideIndex - 1 + slides.length) % slides.length;
  sliderInner.style.transform = `translateX(-${slideIndex * slideWidth}px)`;
});

nextBtn.addEventListener('click', () => {
  slideIndex = (slideIndex + 1) % slides.length;
  sliderInner.style.transform = `translateX(-${slideIndex * slideWidth}px)`;
});