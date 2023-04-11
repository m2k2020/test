$(document).ready(function(){
    
    $.getJSON('fetch_data/',function(data){
        $('#myDropdown').append("<option value=''>Select</option>");
        $.each(data,function(key,value){
            $('#myDropdown').append("<option value='" + value.id + "'>" + value.name + "</option>");
        })
    })





   $('#myForm').submit(function(e){
        e.preventDefault();
        $name = $("#stname").val();
        $age = $("#stage").val();
        $grade_id = $("#myDropdown").val();

        $.ajax({
            url: 'createStudent/',
            type: 'POST',
            data:{
                'name':$name,
                'age':$age,
                'grade_id':$grade_id,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

            },
            success: function(data){
                alert('Successfully Created Data');
                console.log(data)

                document.getElementById("myForm").reset()
            },
            error: function(data){
                console.log('Error is Occured' + data);
            }
        })

        // alert("Name is " + $name + " and age is " + $age+ " and grade_id is " + $grade_id);
       

        // if ($name !== '' && $age !== '' && $grade_id !== ''){
        // //    $('#nameError').text("Please select a name for this student");
        //     alert("Success!");
        //     document.getElementById("myForm").reset();
        //     $('#nameError').text("");
        //     $('#ageError').text("");
        //     $('#gradeError').text("")
        // }
        // else{
        //     $('#nameError').text("Please select a name for this student");
        //     $('#ageError').text("Please select a age for this student");
        //     $('#gradeError').text("Please select a grade for this student");
        // }
   }) 


})


