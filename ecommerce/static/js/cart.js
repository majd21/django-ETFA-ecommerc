

const updateCart = document.getElementById('update-cart')
  updateCart.addEventListener('click' , function(e) {
    e.preventDefault()
    const productId = this.dataset.product
    console.log('productId:' , productId);

    console.log('USER: ' , user)
    if(user === 'AnonymousUser') {
        console.log('User is not logged in...')
    }else {
        console.log('user is logged in and sending data ...')
        updateUserOrder(productId)
    }
})

function updateUserOrder(productId) {
    const form = document.getElementById('updateCartForm')
    // csrftoken = form.getElementsByTagName('input')[0].value
    console.log(form.quantity.value)
    quantityValue = form.quantity.value
    const url = "/update_cart/"
    fetch(url , {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken':csrftoken,
        },
        body: JSON.stringify({
            'productId':productId,
            'quantity': quantityValue
        })
    }).
    then((res) =>  res.json())
    .then(data => {
        console.log('Success:' , data)
        alert('Product Added to cart!')

        location.reload()
    })
}