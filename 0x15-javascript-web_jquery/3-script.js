//  script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header
//  You can’t use document.querySelector to select the HTML tag
const $ = window.$;
if ($('DIV#red_header')) {
  $('DIV#red_header').click(function () {
    $('header').addClass('red');
  });
}
