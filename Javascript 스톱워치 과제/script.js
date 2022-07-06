const $secTime = document.querySelector(".secTime");
const $milTime = document.querySelector(".milTime");
const $startBtn = document.querySelector(".startBtn");
const $stopBtn = document.querySelector(".stopBtn");
const $resetBtn = document.querySelector(".resetBtn");
const $clearBtn = document.querySelector(".clearBtn");
const $recordList = document.querySelector(".recordList");
const $allCheck = document.querySelector(".allCheckBox");

let IntervalID;
let sec = 0;
let milSec = 0;

increTime = function () {
  if (milSec < 99) {
    milSec++;
    $milTime.innerHTML = milSec < 10 ? "0" + milSec : milSec;
  } else {
    milSec = 0;
    $milTime.innerHTML = "00";
    sec++;
    $secTime.innerHTML = sec < 10 ? "0" + sec + ":" : sec + ":";
  }
};

$startBtn.addEventListener("click", function () {
  clearInterval(IntervalID);
  IntervalID = setInterval(increTime, 10);
});

$stopBtn.addEventListener("click", function () {
  clearInterval(IntervalID);

  let container = document.createElement("div");
  let checkBox = document.createElement("input");
  checkBox.setAttribute("type", "checkbox");
  checkBox.setAttribute("class", "checkBox");

  let timeRecord = document.createElement("li");
  timeRecord.setAttribute("class", "timeRecord");
  timeRecord.innerHTML = $secTime.innerHTML + $milTime.innerHTML;

  container.appendChild(checkBox);
  container.appendChild(timeRecord);
  $recordList.appendChild(container);
});

$resetBtn.addEventListener("click", function () {
  clearInterval(IntervalID);
  sec = 0;
  milSec = 0;
  $secTime.innerHTML = "00:";
  $milTime.innerHTML = "00";
});

selectAll = function () {
  let checkedBox = document.querySelectorAll("input[type='checkbox']");
  if ($allCheck.checked) {
    for (let i = 0; i < checkedBox.length; i++) {
      checkedBox[i].checked = true;
    }
  } else {
    for (var i = 0; i < checkedBox.length; i++) {
      checkedBox[i].checked = false;
    }
  }
};

$allCheck.addEventListener("click", function () {
  selectAll();
});

clearRecord = function () {
  let checkedBox = document.querySelectorAll("input[type='checkbox']");
  for (var i = 0; i < checkedBox.length; i++) {
    if (checkedBox[i] != $allCheck) {
      if (checkedBox[i].checked) {
        checkedBox[i].parentElement.remove();
      }
    }
  }
};

$clearBtn.addEventListener("click", function () {
  clearRecord();
});
