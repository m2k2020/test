$(document).ready(function(){
    
    $.getJSON('fetch_data/',function(data){
        $('#myDropdown').append("<option >Select</option>");
        $.each(data,function(key,value){
            $('#myDropdown').append("<option value='" + value.id + "'>" + value.name + "</option>");
        })
    })

   $("#createStudent").on('click',function(){
        $name = $("#stname").val();
        $age = $("#stage").val();
        $grade_id = $("#myDropdown").val();

        if ($name == "" && $age == "" && $grade_id == ""){
            alert("Please select The Balnk space ");
        }
   }) 


})


