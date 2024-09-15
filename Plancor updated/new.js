let currentSlide = 0;

function moveSlide(n) {
    let slides = document.querySelectorAll('.slide');
    currentSlide = (currentSlide + n + slides.length) % slides.length;
    document.querySelector('.slider').style.transform = `translateX(-${currentSlide * 100}%)`;
}

function openModal(productIndex) {
    const modal = document.getElementById('modal');
    const modalInfo = document.getElementById('modal-info');

    const productDetails = {
        1: {name: 'Product 1', description: 'Details about Product 1.'},
        2: {name: 'Product 2', description: 'Details about Product 2.'},
        3: {name: 'Product 3', description: 'Details about Product 3.'}
    };

    modalInfo.innerHTML = `<h3>${productDetails[productIndex].name}</h3><p>${productDetails[productIndex].description}</p>`;
    modal.style.display = 'flex';
}

function closeModal() {
    document.getElementById('modal').style.display = 'none';
}
