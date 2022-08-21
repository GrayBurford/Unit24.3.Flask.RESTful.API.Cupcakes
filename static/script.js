
const base_url = 'http://127.0.0.1:5000/';
const $ccList = $('#cupcake-list');
const $form = $('#form')
const $flavor = $('#flavorInput')
const $size = $('#sizeInput')
const $rating = $('#ratingInput')
const $image = $('#imageInput')

// appends cupcake data to home page UL
async function appendCupcakes() {
    const response = await axios.get(base_url + '/api/cupcakes');
    const rawCupcakeData = response.data.cupcakes;
    const formattedCupcakeData = rawCupcakeData.map(cc => cupcakeMarkUp(cc));
    formattedCupcakeData.map(cc => $ccList.append(cc));
}

// converts object cupcake data into HTML
function cupcakeMarkUp(cc) {
    const flavor = capitalizeFirstLetter(cc.flavor);
    const id = cc.id;
    const image = cc.image;
    const rating = cc.rating;
    const size = capitalizeFirstLetter(cc.size);
    return `<li data-id="${id}">
        ${flavor} -- ${size} -- ${rating}
        <img class="img" src="${image}" alt="(no img)">
    </li>`
}

// capitalizes first letter of a string and floors the rest
function capitalizeFirstLetter(string) {
    const first = string[0].toUpperCase();
    const rest = string.slice(1).toLowerCase();
    return `${first}${rest}`
}

// handles cupcake form submission
async function handleFormSubmission (evt) {
    evt.preventDefault();
    console.log("Form submitted")

    let flavor = $flavor.val();    
    let size = $size.val();
    let rating = $rating.val();
    let image = $image.val();

    let ccData = {
        flavor : flavor,
        size : size,
        rating : rating,
        image : image
    };

    $flavor.val('');
    $size.val('');
    $rating.val('');
    $image.val('');

    await axios.post(base_url + '/api/cupcakes', ccData);
    $ccList.append(cupcakeMarkUp(ccData));
    return;
}


appendCupcakes()
$form.on('submit', handleFormSubmission)
