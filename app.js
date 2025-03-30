document.addEventListener("DOMContentLoaded", function () {
    var homeSwiper = new Swiper(".homeSwiper", {
        loop: true,
        autoplay: { delay: 2500 },
        pagination: { el: ".swiper-pagination", clickable: true },
        navigation: { nextEl: ".swiper-button-next", prevEl: ".swiper-button-prev" }
    });

    var analyzerSwiper = new Swiper(".mySwiper", {
        loop: true,
        autoplay: { delay: 2500 },
        pagination: { el: ".swiper-pagination", clickable: true },
        navigation: { nextEl: ".swiper-button-next", prevEl: ".swiper-button-prev" }
    });
});
