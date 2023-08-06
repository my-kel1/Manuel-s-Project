const audioPlayer = document.querySelector('.audioMP3') // for lyrics line 1
const audioPlayerB = document.querySelector('.audioMP3') // for lyrics line 2
const hymnLyrics = document.querySelector('.hymnLyrics') // for lyrics line 1
const hymnLyricsB = document.querySelector('.hymnLyricsB') // for lyrics line 2
const perline = hymnLyrics.textContent.trim().split('\n') // for lyrics line 1
const perlineB = hymnLyricsB.textContent.trim().split('\n') // for lyrics line 2

// for lyrics line 1
hymnLyrics.removeAttribute('style') 
hymnLyrics.innerText = ''

// for lyrics line 2
hymnLyricsB.removeAttribute('style')
hymnLyricsB.innerText = ''

// store data for lyrics 1 and 2
let syncLyrics = []
let syncLyricsB = []

// for lyrics line 1
// get the value in class=hymnLyrics and store it
perline.map((perline, index) => {
    const [time, text] = perline.trim().split('|')
    syncLyrics.push({'start': time.trim(), 'text': text.trim()})
})

// for lyrics line 2
// get the value in class=hymnLyricsB and store it
perlineB.map((perlineB, index) => {
    const [time, text] = perlineB.trim().split('|')
    syncLyricsB.push({'start': time.trim(), 'text': text.trim()})
})

// for lyrics line 1
// show lyrics in website
audioPlayer.addEventListener('timeupdate', () => {
   syncLyrics.forEach((item) => {
        console.log(item)
        if (audioPlayer.currentTime >= item.start) hymnLyrics.innerText = item.text
    })
})

// for lyrics line 2
// show lyrics in website
audioPlayerB.addEventListener('timeupdate', () => {
    syncLyricsB.forEach((item) => {
         console.log(item)
         if (audioPlayerB.currentTime >= item.start) hymnLyricsB.innerText = item.text
     })
 })