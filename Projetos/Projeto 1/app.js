function changeImg() {
    const image = document.getElementById('image');
    const despt = document.getElementById('description')

    if (image.getAttribute('src') === 'reacts/happy.jpg') {
        despt.innerText = 'Hungry Fausto';
        image.src = 'reacts/hungry.jpg';
    } else if (image.getAttribute('src') === 'reacts/hungry.jpg') {
        despt.innerText = 'Reflexive Fausto';
        image.src = 'reacts/reflexive.jpg';
    } else if (image.getAttribute('src') === 'reacts/reflexive.jpg') {
        despt.innerText = 'Surprised Fausto';
        image.src = 'reacts/surprised.jpg';
    } else {
        despt.innerText = 'Happy Fausto';
        image.src = 'reacts/happy.jpg';
    }
};