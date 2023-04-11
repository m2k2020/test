$(document).ready(function(){
    
    $.getJSON('fetch_data/',function(data){
        $('#myDropdown').append("<option value=''>Select</option>");
        $.each(data,function(key,value){
            $('#myDropdown').append("<option value='" + value.id + "'>" + value.name + "</option>");
        })
    })

   $("#createStudent").on('click',function(){
        $name = $("#stname").val();
        $age = $("#stage").val();
        $grade_id = $("#myDropdown").val();

        if ($name !== '' && $age !== '' && $grade_id !== ''){
        //    $('#nameError').text("Please select a name for this student");
            alert("Success!");
            document.getElementById("myForm").reset();
            $('#nameError').text("");
            $('#ageError').text("");
            $('#gradeError').text("")
        }
        else{
            $('#nameError').text("Please select a name for this student");
            $('#ageError').text("Please select a age for this student");
            $('#gradeError').text("Please select a grade for this student");
        }
   }) 


})


