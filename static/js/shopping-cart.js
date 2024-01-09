function addToShoppingCart(productId){
    console.log(productId);
    $.get('order/add-to-shopping-cart?product_id='+ productId).then(res => {
        console.log(res);
    });
}