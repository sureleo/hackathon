(function() {
    "use strict";
    $(document).on('ready', function() {
        $('#lucky').on('click', function() {
            location.reload();
        });
        $('#lucky').on('mousedown', function() {
            $(this).text('ヾ(*ΦωΦ)ツ');
        });
    });
}());
