$(document).ready(function(){

    if($('#stresult') != null){
        readStudent();
    }
    
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
                readStudent()
            },
            error: function(data){
                console.log('Error is Occured' + data);
            }
        })
   }) 


   $(document).on('click', '.studentedit', function(){
    $id = $(this).attr('name');
    window.location = "editStudent/" + $id;

});

$('#updateForm').submit(function(e){
    e.preventDefault();
    $id = $('#id').val();
    $name = $("#name").val();
    $age = $("#age").val();
    $grade_id = $("#umyDropdown").val();

    console.log('id = '+$id + 'name = '+$name+'class id ='+$grade_id)
})


})


function readStudent(){
    $.ajax({
        url: "readStudent/",
        type: "POST",
        async: false,
        data:{
            res : 1,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $('#stresult').html(response)
        }
    })

}

