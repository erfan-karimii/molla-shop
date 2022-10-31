/**
 * Theme: Unikit - Responsive Bootstrap 5 Admin Dashboard
 * Author: Mannatthemes
 * Tour Js
 */

(function(){

  var tour = {
    id: "welcome_tour",
    steps: [
      {
        title: "سوالات متداول",
        content: "آیا سوالی دارید؟",
        target: "#tourFaq",
        placement: "top"
      },
      {
        title: "Color Card",
        content: "This is the color cards.",
        target: document.querySelector("#bg_colorCard"),
        placement: "bottom"
      }
    ],
    showPrevButton: true,
    scrollTopMargin: 100
  };

  // Start the tour!
  hopscotch.startTour(tour);
})();

  