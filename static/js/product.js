
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');
const sliderInner = document.querySelector('.product-slider-inner');
const slides = document.querySelectorAll('.product-item');
const slideWidth = slides[0].offsetWidth;
let slideIndex = 0;

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

const contentBox = document.getElementById('content-box');

fetch('../../uploads/output.txt')
  .then(response => response.text())
  .then(text => {
    contentBox.innerHTML = text;
  })
  .catch(error => {
    console.error('Error loading text file:', error);
  });
