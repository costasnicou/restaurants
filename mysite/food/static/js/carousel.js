const carouselSlide = document.querySelector('.carousel-slide');
const images = document.querySelectorAll('.carousel-slide img');
const modal = document.getElementById('zoomModal');
const zoomedImage = document.getElementById('zoomedImage');
const closeModal = document.querySelector('.close');

let counter = 0;
const size = images[0].clientWidth;

// Carousel navigation
document.getElementById('nextBtn').addEventListener('click', () => {
    if (counter >= images.length - 1) return;
    carouselSlide.style.transform = `translateX(${-size * (counter + 1)}px)`;
    counter++;
});

document.getElementById('prevBtn').addEventListener('click', () => {
    if (counter <= 0) return;
    carouselSlide.style.transform = `translateX(${-size * (counter - 1)}px)`;
    counter--;
});

// Zoom functionality
images.forEach(image => {
    image.addEventListener('click', () => {
        modal.style.display = "block";
        zoomedImage.src = image.src; // Set the modal image to the clicked image's src
    });
});

// Close the modal
closeModal.addEventListener('click', () => {
    modal.style.display = "none";
});

// Close the modal if the user clicks outside the image
window.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.style.display = "none";
    }
});
