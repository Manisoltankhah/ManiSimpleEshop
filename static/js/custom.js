function sendArticleComment(articleId) {
    var comment = $('#commentText').val();
    var parentId = $('#parent_id').val();
    console.log(parentId);
    $.get('/article/add-article-comment', {
        article_comment: comment,
        article_id: articleId,
    }).then(res => {
        console.log(res);
    });
}

function sendProductComment(productId) {
    var comment = $('#commentTextProduct').val()
    var parentId = $('#parent_id').val();
    console.log(parentId)
    $.get('/products/add_product_comment', {
        product_comment: comment,
        product_id: productId,
    }).then(res => {
        console.log(res);
    });
}

function fillParentId(parentId) {
    $('#parent_id').val(parentId);
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"});
}

function filterProducts(){
    const filterPrice = $('#sl2').val();
    const start_price = filterPrice.split(',')[0];
    const end_price = filterPrice.split(',')[1];
    $('#start_price').val(start_price);
    $('#end_price').val(end_price);
    $('#filter-form').submit();
}

function fillPage(page){
    $('#page').val(page);
    $('#filter-form').submit();
}

function ShowLargeImage(imageSrc){
    $('#main_image').attr('src', imageSrc);
    $('#show_large_image_modal').attr('href', imageSrc);
}

function addProductToOrder(productId) {
    const productCount = $('#product-count').val();
    $.get('/cart/add-to-shopping-cart?product_id=' + productId + '&count=' + productCount).then(res => {
        Swal.fire({
              title: 'پیام',
              text: res.text,
              icon: res.icon,
              showCancelButton: false,
              confirmButtonColor: '#3085d6',
              cancelButtonColor: '#d33',
              confirmButtonText: res.confirm_button_text
});
    })
}

function removeOrderDetail(detailId){
    $.get('/user-panel/remove-order-detail?detail_id=' + detailId).then(res => {
        if(res.status === 'success'){
            $('#order-detail-content').html(res.body)
        }
    })
}

function changeOrderDetailCount(detailId, state) {
    $.get('/user-panel/change-order-detail?detail_id=' + detailId + '&state=' + state).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
            window.location.href = 'http://localhost:8080/user-panel/user-cart'
        }
    });
    // window.location.href = 'http://127.0.0.1:8080/user-panel/user-cart'
}






















