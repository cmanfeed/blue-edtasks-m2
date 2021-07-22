const tasks = document.querySelectorAll('.task');

tasks.forEach((task) => {
    task.addEventListener('click', () =>{
        if (task.style.textDecoration === 'line-through'){
            task.style.textDecoration = 'none';
        }else{
            task.style.textDecoration = 'line-through'
        }

        ;
    })
})