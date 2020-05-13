$(document).ready(function () {
    'use strict';
    income();
    expences();
    all();
    openMerch();
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