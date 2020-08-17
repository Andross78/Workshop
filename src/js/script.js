$(document).ready(function(){ 

    $('.button_reset').click(function(event) {
        alert("Potwierdzenie zresetowania hasła zostało wysłane");
    });

    $('ul.catalog__tabs').on('click', 'li:not(.catalog__tab_active)', function() {
        $(this)
          .addClass('catalog__tab_active').siblings().removeClass('catalog__tab_active')
          .closest('div.container').find('div.catalog__content').removeClass('catalog__content_active').eq($(this).index()).addClass('catalog__content_active');
    });

    function toggleSlide(item) {
        $(item).each(function(i) {
            $(this).on('click', function(e) {
                e.preventDefault();
                $('.catalog-item__content').eq(i).toggleClass('catalog-item__content_active');
                $('.catalog-item__list').eq(i).toggleClass('catalog-item__list_active');
            })
        });
    };

    $('ul.account__tabs').on('click', 'li:not(.account__tab_active)', function() {
        $(this)
          .addClass('account__tab_active').siblings().removeClass('account__tab_active')
          .closest('div.container').find('div.account__content').removeClass('account__content_active').eq($(this).index()).addClass('account__content_active');
    });

    toggleSlide('.catalog-item__link');
    toggleSlide('.catalog-item__back');

    // Modal window

    $('[data-modal=consultation]').on('click', function() {
        $('.overlay, #consultation').fadeIn('slow');
    });
    $('.modal__close').on('click', function() {
        $('.overlay, #consultation, #thanks, #order, #car, #car-edit').fadeOut('slow');
    });

    $('.button_mini').each(function(i) {
        $(this).on('click', function() {
            $('#order .modal__descr').text($('.catalog-item__subtitle').eq(i).text());
            $('.overlay, #order').fadeIn('slow');
        })
    });

    $('.button_car').on('click', function() {
        $('.overlay, #car').fadeIn('slow');
    });

    $('.button_edit').each(function(i) {
        $(this).on('click', function() {
            $('.overlay, #car-edit').fadeIn('slow');
        })
    });

    // Smooth scroll and page up

    $(window).scroll(function() {
        if ($(this).scrollTop() > 1200) {
            $('.pageup').fadeIn();
        } else {
            $('.pageup').fadeOut();
        }
    });

    $("a[href^='#up']").click(function(){
        const _href = $(this).attr("href");
        $("html, body").animate({scrollTop: $(_href).offset().top+"px"});
        return false;
    });

    new WOW().init();

});