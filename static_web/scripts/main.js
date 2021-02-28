
function getMoodClass(mood) {
    let moodClass = 'neutral';

    if (mood > 0) {
        moodClass = 'semi-happy';
        if (mood >= 0.5) {
            moodClass = 'happy';
        }
    } else if (mood < 0) {
        moodClass = 'semi-unhappy';
        if (mood <= -0.5){
            moodClass = 'unhappy'
        }
    }
    return moodClass;
}

$(() => {
    $('#calendar').calendar({
        maxYear: 1
    });

    eel.get_mood_dictionary()()
        .then(moodDictionary => {
            $main = $('.main');

            for (const date in moodDictionary) {
                const [month, day, year] = date.split('/');
                const mood = getMoodClass(moodDictionary[date]);
                $calendarItem = $(`.jqyc-day-${day}.jqyc-day-of-${month}-month`).addClass(mood);
            }
        });
});