function genButton(val) {
	
	let button = document.createElement("button");
	
	let classAttr = document.createAttribute("class");
	classAttr.value = "btn btn-primary";
	let dataBsToggleAttr = document.createAttribute("data-bs-toggle");
	dataBsToggleAttr.value = "button";
	let idAttr = document.createAttribute("id");
	idAttr.value = "answer-" + val;
	
	button.setAttributeNode(classAttr);
	button.setAttributeNode(dataBsToggleAttr);
	button.setAttributeNode(idAttr);
	
	return button;
}

function genVertButtonGroup() {
	let box = document.createElement("div");
	let classAttr = document.createAttribute("class");
	classAttr.value = "d-grid gap-2 col-6 mx-auto";
	box.setAttributeNode(classAttr);

	for (let i=0;i<4;i++) {
		const button = genButton(i);
		box.appendChild(button);
	}
	
	return box;
}

function renderQuestion() {
	let box = document.createElement("div");
	let classAttr = document.createAttribute("class");
	classAttr.value = "row";
	
	let quesText = document.createElement("h4");
	let idAttr = document.createAttribute("id");
	idAttr.value = "question"
	
	box.setAttributeNode(classAttr);
	quesText.setAttributeNode(idAttr);

	box.appendChild(quesText);

	return box;
}

function createDivBox() {
	const question = renderQuestion();
	const answerButtons = genVertButtonGroup();
	
	let box = document.createElement("div")
	let classAttr = document.createAttribute("class");
	classAttr.value = "row";
	box.setAttributeNode(classAttr);
	
	let boxCol = document.createElement("div")
	let boxColClassAttr = document.createAttribute("class");
	classAttr.value = "col-lg-6 m-auto border border-3";
	boxCol.setAttributeNode(boxColClassAttr);
	
	boxCol.appendChild(question);
	boxCol.appendChild(answerButtons);
	box.appendChild(boxCol);

	return box;
}

function generateQuestions () {
	for (let i=0;i<10;i++) {
		let box = createDivBox();
		document.getElementById('test-area').appendChild(box);
	}
}
