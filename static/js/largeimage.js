function ShowLargeImage(imageSrc){
    console.log(imageSrc);
    $('#main_image').attr('src', imageSrc);
    $('#show_large_image').attr('href', imageSrc);
}