$(function() {
    // Sidebar toggle behavior
              $('#sidebarCollapse').on('click', function() {
                   $('#sidebar, #content').toggleClass('active');
               });
              });

$(function() {
     // Sidebar toggle behavior
                 $('#sidebarCollapse-small').on('click', function() {
                     $('#sidebar, #content').toggleClass('active');
                     });
                });
$(function() {
    //btn add giảng viên 
            $('#icon_add-teacher--project').on('click', function() {
                const icon = $('#add_teacher--project');
                console.log(icon);
                const icon_1 = $('add_teacher--project-on');
                console.log(icon_1);
                $( '#add_teacher--project').toggleClass('add_teacher--project-on');
            })
})
$(function() {
    //btn add giảng viên 
            $('#icon_add-student--project').on('click', function() {
                const icon = $('#add_teacher--project');
                console.log(icon);
                const icon_1 = $('add_teacher--project-on');
                console.log(icon_1);
                $( '#add_student--project').toggleClass('add_student--project-on');
            })
})







