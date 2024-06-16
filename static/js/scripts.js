document.addEventListener('DOMContentLoaded', async () => {
    const response = await fetch('/marathons/');
    const marathons = await response.json();
    const scheduleList = document.getElementById('schedule-list');
    
    marathons.forEach(marathon => {
        const listItem = document.createElement('li');
        listItem.textContent = `${marathon.name} - ${marathon.date}`;
        listItem.addEventListener('click', () => {
            alert(`Marathon: ${marathon.name}\nDate: ${marathon.date}\nOverview: ${marathon.overview}\nRoute: ${marathon.route}`);
        });
        scheduleList.appendChild(listItem);
    });
});
