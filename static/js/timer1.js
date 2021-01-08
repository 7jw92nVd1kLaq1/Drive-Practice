const countDownDate = Math.floor((new Date().getTime()) / 1000) + (60 * 20);
let sec = 59;

setInterval(function () {
	const nowTime = Math.floor((new Date().getTime()) / 1000);
	let diff = countDownDate - nowTime;
	let min = Math.floor(diff / 60);
	
	const strSec = `${sec}`.padStart(2, '0');

	document.getElementById("text-time").innerHTML = `남은시간: ${min}:${strSec}`;
	document.getElementById("text-time-20").innerHTML = `남은시간: ${min}:${strSec}`;
	
	sec--;
	
	if (sec < 0) {
		if (min === 0) {
			document.getElementById("test-cont").submit();
		} else {
			sec = 59;
		}
	}
}, 1000);
