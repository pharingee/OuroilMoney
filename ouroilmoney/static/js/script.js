$(document).ready(function () {
   $('.button-collapse').sideNav();
   $('.dropdown-button').dropdown();
   console.log($('.tabs-wrapper .table-of-contents'));
   if ($('.tabs-wrapper .table-of-contents').length > 0) {
      $('.tabs-wrapper .table-of-contents').pushpin({ top: $('.tabs-wrapper').offset().top });
   }
});
