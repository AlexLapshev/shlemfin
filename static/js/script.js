$(document).ready(function () {
    'use strict';
    income();
    expences();
    all();
    openMerch();
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
        $.ajax({
            type: 'POST',
            url: '/',
            data: {
                product: $('#id_product').val(),
                value: $('#id_value').val(),
                title: $('#id_title').val(),
                operation: $('#id_operation').val(),
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function () {
                $(".success-add").show(800);
                $('.new-finance-form')[0].reset();
                setTimeout(
                    function () {
                        $(".success-add").hide(800)
                    }, 3000);
            }
        })
    });
}

