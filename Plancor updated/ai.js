const imageUpload = document.getElementById('imageUpload');
const imagePreview = document.getElementById('imagePreview');
const submitBtn = document.getElementById('submitBtn');

imageUpload.addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
            imagePreview.src = e.target.result;
            imagePreview.style.display = 'block';
        }

        reader.readAsDataURL(file);
    }
});

submitBtn.addEventListener('click', function () {
    if (!imageUpload.files[0]) {
        alert('Please upload an image before submitting.');
    } else {
        
        alert('Image submitted successfully!');
    }
});