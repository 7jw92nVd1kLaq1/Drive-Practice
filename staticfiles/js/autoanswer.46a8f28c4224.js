let questions = {};


function getAllTheButtons(list) {
	for (let i=0; i<list.length; i++) {
		
		if (list[i].nodeName == "BUTTON") {
			const parentElem = list[i].parentNode.getAttribute("id");
			
			if (parentElem in questions) {
				if (!questions[parentElem].includes(list[i])) {
					questions[parentElem].push(list[i]);
				}
			} else {
				questions[parentElem] = [];
				questions[parentElem].push(list[i]);
			}

			if (questions[parentElem].length > 2) {
				//console.log(questions[parentElem]);
				questions[parentElem][0].setAttribute("class", "btn btn-primary mt-1");
				questions[parentElem][0].setAttribute("aria-pressed", "false");
				questions[parentElem].shift();
			}
		}
	}
}


function cleanArray() {
	for (const answerArr in questions) {
		for (let i=0; i<questions[answerArr].length; i++) {
			let attr = questions[answerArr][i].getAttribute("class");
			if (attr.indexOf("active") < 0) {
				questions[answerArr].splice(i, 1);
			}
		}
	}
}


function currentValue(arr) {
	const tempArr = [];
	
	for (let i=0; i<arr.length; i++) {
		tempArr.push(arr[i].getAttribute("value"));
	}

	return tempArr.sort().join('');
}


function changeValue() {
	for (const each in questions) {
		const updatedValue  = currentValue(questions[each]);
		
		const input = each.replace(/[^0-9]/g, '');
		document.getElementById(`answer_${input}`).setAttribute("value", updatedValue);
		if (updatedValue.length == 2) {
			const newValue = updatedValue.substr(0,1) + ", " + updatedValue.substr(1,1);
			document.getElementById(`selected-answer-${input}`).innerHTML = newValue;
			document.getElementById(`answer-for-${input}-20`).innerHTML = `${input}. ${newValue}`;
			
			if (document.getElementById(`answer-for-${input}-40`)) {
				document.getElementById(`answer-for-${input}-40`).innerHTML = `${input}. ${newValue}`;
			}
		} else {
			document.getElementById(`selected-answer-${input}`).innerHTML = updatedValue;
			document.getElementById(`answer-for-${input}-20`).innerHTML = `${input}. ${updatedValue}`;

			if (document.getElementById(`answer-for-${input}-40`)) {
				document.getElementById(`answer-for-${input}-40`).innerHTML = `${input}. ${updatedValue}`;
			}
		}
		const elem = document.getElementById(`answer_${input}`).getAttribute("value");
		console.log(elem);
		
	}
}


function checkToggle() {
	cleanArray();
	getAllTheButtons(document.getElementsByClassName("active"));
	changeValue();	
	console.log(questions);
}


function submitTest() {
	document.getElementById('test-cont').submit();
}
