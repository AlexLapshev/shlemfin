$(document).ready(function () {
    'use strict';
    income();
    expences();
    all();
    openMerch();
    chooseProduct();
    ajaxAdd();
});

function filterButton() {
    $('.btns-f').children().each(function () {
        $(this).removeClass('active')
    });
}

function income() {
    const allF = $('.list-oper');
    $('.btn-filter:nth-child(2)').on('click', () => {
            filterButton();
            allF.each(function () {
                $(this).removeClass('d-none');
                $(this).addClass('d-flex');
                if ($(this).children().eq(2).text().trim() !== 'Доход') {
                    $(this).removeClass('d-flex');
                    $(this).addClass('d-none');
                }
            });
        }
    );
}

function expences() {
    const allF = $('.list-oper');
    $('.btn-filter:nth-child(3)').on('click', () => {
        filterButton();
        allF.each(function () {
            $(this).removeClass('d-none');
            $(this).addClass('d-flex');
            if ($(this).children().eq(2).text().trim() === 'Доход') {
                $(this).removeClass('d-flex');
                $(this).addClass('d-none');
            }
        })
    });
}

function all() {
    const allF = $('.list-oper');
    $('.btn-filter:nth-child(1)').on('click', () => {
        allF.each(function () {
            $(this).removeClass('d-none');
            $(this).addClass('d-flex');
        })
    });
}

function openMerch() {
    $('.btn-merch').on('click', function () {
        $(this).next().toggleClass('d-none')
    })
}


function ajaxAdd() {
    $('.new-finance-form').on('submit', function (event) {
            event.preventDefault();
            let size = $('.active-select').children('select').children('option:selected').val();
            console.log(size);

            if (size.length > 3) {
                alert('Выберите Размер')
            }
            else {
                $.ajax({
                    type: 'POST',
                    url: '/',
                    data: {
                        product: $('#id_product').val(),
                        price: $('#id_price').val(),
                        size: size,
                        optional_info: $('#id_optional_info').val(),
                        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
                    },
                    success: function () {
                        $(".success-add").show(800);
                        $('.new-finance-form')[0].reset();
                        setTimeout(
                            function () {
                                $(".success-add").hide(800);
                            }, 3000);
                    }
                })
            }
        }
    )
    ;
}

function chooseProduct() {
    $('.img_choice:first').addClass('img_choice-active');
    getIdPrice();
    $('.select-size-hidden:first').removeClass('select-size-hidden');
    $('.select-size-wrapper:first').addClass('active-select');
    $('.img_choice').on('click', function () {
        $('.img_choice').each(function () {
            $(this).removeClass('img_choice-active');
            $('.select-size-wrapper').each(function () {
                $(this).removeClass('select-size-hidden')
            })
        });
        $(this).addClass('img_choice-active');
        let idP = $(this).next('.img_id').val();
        $('.select-size-wrapper').each(function () {
            $(this).removeClass('active-select');
            $(this).removeClass('select-size-hidden');
            idS = $(this).children('input').val();
            if (idS !== idP) {
                $(this).addClass('select-size-hidden');
            }
            else {
                $(this).addClass('active-select');
            }
        });
        getIdPrice();
    })
}

function getIdPrice() {
    let productId = $('.img_choice-active').next('.img_id').val();
    let productPrice = $('.img_choice-active').nextAll('.img_price').val();
    $('#id_price').val(productPrice);
    $('#id_product').val(productId)
}