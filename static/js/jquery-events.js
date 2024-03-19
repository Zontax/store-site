// Коли html документ (завантажено)
$(document).ready(function () {
    var notification = $('#notification') // елемент по id - сповіщення від django

    if (notification.length > 0) {
        // І через 7 сек. прибираєм
        setTimeout(function () {
            notification.alert('close')
        }, 3500)
    }

    // Коли клікаєм на корзину то відкриваєм модальне вікно
    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body')
        $('#exampleModal').modal('show')
    })

    // Подія (клік по кнопці) закрити вікно корзини
    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide')
    })

    // Обробник подій радіокнопки вибору способу доставки
    $("input[name='requires_delivery']").change(function () {
        var selectedValue = $(this).val()
        // прибираєм або відображаєм input ввода адреса доставки
        if (selectedValue === '1') {
            $('#deliveryAddressField').show()
        } else {
            $('#deliveryAddressField').hide()
        }
    })
})
