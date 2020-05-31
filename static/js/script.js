$(document).ready(function () {
    'use strict';
    selectProduct();
    ajaxAdd();
    showPanel();
    sendTo()
});


function selectProduct() {
    $('.pro-id-size:first').next('.select-size').removeClass('d-none');
    $('.select-size:first').addClass('select-size-active');
    let selectImg = $('.select-img');
    $('#id_price').val($(selectImg).first().children('input').val());
    $('#select-img__selected').val($(selectImg).first().next().val());
    $(selectImg).first().addClass('select-img-active');
    $(selectImg).on('click', function () {
        $('#id_price').val($(this).children('input').val());
        $(selectImg).each(function () {
            $(this).removeClass('select-img-active');
        });
        $(this).addClass('select-img-active');
        let productId = $(this).next().val();
        $('#select-img__selected').val(productId);
        $('.pro-id-size').each(function () {
            $(this).next('.select-size').addClass('d-none');
            $(this).next('.select-size').removeClass('select-size-active');
            if ($(this).val() === $('#select-img__selected').val()) {
                $(this).next('.select-size').removeClass('d-none');
                $(this).next('.select-size').addClass('select-size-active');
            }
        });
    });
}


function ajaxAdd() {
    $('.select-size-form').on('submit', function (event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/',
            data: {
                product: $('#select-img__selected').val(),
                price: $('#id_price').val(),
                size: $('.select-size-active').children('option:selected').val(),
                optional_info: $('#id_optional_info').val(),
                operation: $('#id_operation').val(),
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function () {
                $(".success-add").show(800);
                $('.select-size-form')[0].reset();
                setTimeout(
                    function () {
                        $(".success-add").hide(800);
                    }, 3000);
            }
        })
    });
}

function showPanel() {
    $('.openning-btn').on('click', function () {
        $(this).next().toggleClass('d-none');
    })
}

function sendTo() {
    $('.send-to-form').on('submit', function (event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/sendto/',
            data: {
                fcs: $('#id_fcs').val(),
                where: $('#id_where').val(),
                send_description: $('#id_send_description').val(),
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: () => {
                $('.send-to-form')[0].reset();

            }
        })
    })
}
