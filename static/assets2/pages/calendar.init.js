/**
* Theme: Unikit - Responsive Bootstrap 5 Admin Dashboard
* Author: Mannatthemes
* Component: Full-Calendar
*/


document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
    defaultDate: '1400-06-12',
    locale:'fa',
    timeZone: 'Asia/Tehran',
    initialView: 'dayGridMonth',
    editable: true,
    selectable: true,
    events: [
      {
        title: 'ناهار کاری',
        start: '1400-06-03T13:00:00',
        constraint: 'businessHours',
        className: 'bg-soft-warning',
      },
      {
        title: 'ملاقات',
        start: '1400-06-13T11:00:00',
        constraint: 'availableForMeeting', // defined below
        className: 'bg-soft-purple',
        textColor: 'white'
      },
      {
        title: 'کنفرانس',
        start: '1400-06-27',
        end: '1400-06-29',
        className: 'bg-soft-primary',
      },

      {
        title: 'کنفرانس',
        start: '1400-02-27',
        end: '1400-02-29',
        className: 'bg-soft-primary',
      },
      
      // areas where "Meeting" must be dropped
      {
        groupId: 'availableForMeeting',
        start: '1400-06-11T10:00:00',
        end: '1400-06-11T16:00:00',
        title: ' اتفاق تکراری',
        className: 'bg-soft-purple',
      },
      {
        groupId: 'availableForMeeting',
        start: '1400-06-15T10:00:00',
        end: '1400-06-15T16:00:00',
        title: ' تعطیلات',
        className: 'bg-soft-success',
      },

      {
        groupId: 'availableForMeeting',
        start: '1400-02-15T10:00:00',
        end: '1400-02-15T16:00:00',
        title: ' تعطیلات',
        className: 'bg-soft-success',
      },

      // red areas where no events can be dropped
      
      {
        start: '1400-06-06',
        end: '1400-06-08',
        overlap: false,
        title: 'اتفاق جدید',
        className: 'bg-soft-pink',
      }
    ],
  });

  calendar.render();
});

