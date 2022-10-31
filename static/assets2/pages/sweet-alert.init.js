/**
 * Theme: Unikit - Responsive Bootstrap 4 Admin Dashboard
 * Author: Mannatthemes
 * Sweet Alert Js
 */

function executeExample(sub){
    switch(sub){
        case 'basicMessage':
        Swal.fire('هر احمقی می تواند از کامپیوتر استفاده کند')
        return;
        case 'titleText':
            Swal.fire(
                'اینترنت؟',
                'آن چیز هنوز در اطراف است؟',
                'question'
              )
        return;
        case 'errorType':
            Swal.fire({
                icon: 'error',
                title: "اوه...",
                text: 'مشکلی پیش آمد!',
                footer: '<a href>چرا من این مشکل را دارم؟</a>'
              })
        return;

        case 'customHtml':
            Swal.fire({
                title: '<strong> مثال <u> دیگر  </u></strong>',
                icon: 'info',
                html:
                  ' تو میتوانی استفاده کنی <b>متن پر رنگ </b>, ' +
                  '<a href="//sweetalert2.github.io">لینک</a> ' +
                  'و بقیه تگ ها',
                showCloseButton: true,
                showCancelButton: true,
                focusConfirm: false,
                confirmButtonText:
                  '<i class="fa fa-thumbs-up"></i> عالی ! ',
                confirmButtonAriaLabel: 'Thumbs up, great!',
                cancelButtonText:
                  '<i class="fa fa-thumbs-down"></i>',
                cancelButtonAriaLabel: 'Thumbs down'
              })
        return;

        case 'threeButtons':
          Swal.fire({
            title: 'آیا میخواهید تغییرات ذخیره شود؟',
            showDenyButton: true,
            showCancelButton: true,
            confirmButtonText: `ذخیره`,
            confirmButtonText: ` ذخیره نشود`,
          }).then((result) => {
            /* Read more about isConfirmed, isDenied below */
            if (result.isConfirmed) {
              Swal.fire('Saved!', '', 'success')
            } else if (result.isDenied) {
              Swal.fire('تغییرات ذخیره نشد', '', 'info')
            }
          })
        return;

        case 'customPosition':
          Swal.fire({
            position: 'top-end',
            icon: 'success',
            title:'کار شما ذخیره شده است',
            showConfirmButton: false,
            timer: 1500
          })
        return;

        case 'customAnimation':
          Swal.fire({
            title: 'انیمیشن سفارشی با Animate.css',
            showClass: {
              popup: 'animate__animated animate__fadeInDown'
            },
            hideClass: {
              popup: 'animate__animated animate__fadeOutUp'
            }
          })
        return;

        case 'warningConfirm':
          Swal.fire({
            title: 'مطمئنی؟',
            text: "شما نمی توانید این را برگردانید!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'بله حذفش کن!',
          }).then(function(result) {
            if (result.isConfirmed) {
              Swal.fire(
                'حذف شد!',
                'فایل شما حذف شده است',
                'success'
              )
            }
          })
        return;

        case 'handleDismiss':
          const swalWithBootstrapButtons = Swal.mixin({
            customClass: {
              confirmButton: 'btn btn-success',
              cancelButton: 'btn btn-danger me-2'
            },
            buttonsStyling: false
          })
          
          swalWithBootstrapButtons.fire({
            title: 'مطمئنی؟',
            text: "شما نمی توانید این را برگردانید!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'بله حذفش کن!',
            cancelButtonText: 'خیر , لغو !',
            reverseButtons: true
          }).then((result) => {
            if (result.isConfirmed) {
              swalWithBootstrapButtons.fire(
                'حذف شد!',
                'فایل شما حذف شده است',
                'success'
              )
            } else if (
              /* Read more about handling dismissals below */
              result.dismiss === Swal.DismissReason.cancel
            ) {
              swalWithBootstrapButtons.fire(
                'لغو شد',
                "پرونده خیالی شما امن است :)",
                "خطا"
              )
            }
          })
        return;
        
        case 'customImage':
          Swal.fire({
            title: 'Unikit!',
            text: 'مدال با لوگوی برند.',
            imageUrl: 'assets/images/logo-sm.png',
            imageWidth: 80,
            imageHeight: 80,
            imageAlt: 'Custom image',
          })
        return;
        
        case 'customWidth':
          Swal.fire({
            title: 'عرض سفارشی، بالشتک، پس زمینه.',
            width: 600,
            padding: 50,
            background: 'rgba(254,254,254,1) url(assets/images/pattern.png)',
          })
        return;
        
        case 'timer':
          let timerInterval
            Swal.fire({
              title: "هشدار بسته خودکار!",
              html: 'من در <b></b> میلی ثانیه می بندم.',
              timer: 2000,
              timerProgressBar: true,
              didOpen: () => {
                Swal.showLoading()
                timerInterval = setInterval(() => {
                  const content = Swal.getContent()
                  if (content) {
                    const b = content.querySelector('b')
                    if (b) {
                      b.textContent = Swal.getTimerLeft()
                    }
                  }
                }, 100)
              },
              willClose: () => {
                clearInterval(timerInterval)
              }
            }).then((result) => {
              /* Read more about handling dismissals below */
              if (result.dismiss === Swal.DismissReason.timer) {
                console.log('I was closed by the timer')
              }
            })
        return;
        
        case 'rtl':
          Swal.fire({
            title: 'می خواهید ادامه دهید؟',
            icon: 'question',
            iconHtml: '؟',
            confirmButtonText: 'بله',
            cancelButtonText: 'خیر',
            showCancelButton: true,
            showCloseButton: true
          })
        return;
        
        case 'ajaxRequest':
          Swal.fire({
            title: 'نام کاربری گیت هاب خود را ارسال کنید',
            input: 'text',
            inputAttributes: {
              autocapitalize: 'off'
            },
            showCancelButton: true,
            confirmButtonText: 'جستجو',
            showLoaderOnConfirm: true,
            preConfirm: (login) => {
              return fetch(`//api.github.com/users/${login}`)
                .then(response => {
                  if (!response.ok) {
                    throw new Error(response.statusText)
                  }
                  return response.json()
                })
                .catch(error => {
                  Swal.showValidationMessage(
                    `درخواست ناموفق بود: ${error}`
                  )
                })
            },
            allowOutsideClick: () => !Swal.isLoading()
          }).then((result) => {
            if (result.isConfirmed) {
              Swal.fire({
                title: `${result.value.login}'s avatar`,
                imageUrl: result.value.avatar_url
              })
            }
          })
        return;
        
        case 'chainingModals':
          Swal.mixin({
            input: 'text',
            confirmButtonText: "&rarr; بعدی ",
            showCancelButton: true,
            progressSteps: ['1', '2', '3']
          }).queue([
            {
              title: 'سوال 1',
              text: 'زنجیر کردن مدال های آسان است'
            },
            'سوال 2',
            'سوال 3'
          ]).then((result) => {
            if (result.value) {
              const answers = JSON.stringify(result.value)
              Swal.fire({
                title: "همه چیز انجام شد!",
                html: `
                  پاسخ های شما:
                  <pre><span class="code">${answers}</span> </pre>
                `,
                confirmButtonText: 'دوست داشتني!'
              })
            }
          })
        return;
        
        case 'dynamicQueue':
          const ipAPI = '//api.ipify.org?format=json'

          Swal.queue([{
            title: 'IP عمومی شما',
            confirmButtonText: "نمایش IP عمومی من",
            text:
              'IP عمومی شما دریافت خواهد شد' +
              "از طریق درخواست AJAX",
            showLoaderOnConfirm: true,
            preConfirm: () => {
              return fetch(ipAPI)
                .then(response => response.json())
                .then(data => Swal.insertQueueStep(data.ip))
                .catch(() => {
                  Swal.insertQueueStep({
                    icon: 'error',
                    title: 'نمی توان IP عمومی شما را دریافت کرد'
                  })
                })
            }
          }])
        return;
        
        case 'mixin':
          const Toast = Swal.mixin({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            timer: 3000,
            timerProgressBar: true,
            didOpen: (toast) => {
              toast.addEventListener('mouseenter', Swal.stopTimer)
              toast.addEventListener('mouseleave', Swal.resumeTimer)
            }
          })
          
          Toast.fire({
            icon: 'success',
            title: 'با موفقیت وارد سیستم شد'
          })
        return;
        
        case 'declarativeTemplate':
          
          Swal.fire({
            template: '#my-template',
          })          
        return;
        
        case 'TriggerModalToast':
          Swal.bindClickHandler()
          Swal.mixin({
            toast: true,
          }).bindClickHandler('data-swal-toast-template')
        return;

        case 'success':
          Swal.fire({
            icon: 'success',
            title:'کار شما ذخیره شده است',
            timer: 1500
            })
        return;
        
        case 'error':
          Swal.fire({
              icon: 'error',
              title: "اوه...",
              text: 'مشکلی پیش آمد!',
            })
        return;
        case 'warning':
          Swal.fire({
              icon: 'warning',
              title: "اوه...",
              text: 'آیکون هشدار !',
            })
        return;
        case 'info':
          Swal.fire({
              icon: 'info',
              title: "اوه...",
              text: 'آیکون اطلاعات !',
            })
        return;

        case 'question':
          Swal.fire({
              icon: 'question',
              title: "اوه...",
              text: 'آیکون سوال !',
            })
        return;

    }
}