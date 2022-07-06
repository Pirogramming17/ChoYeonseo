const $secTime = document.querySelector(".secTime");
const $milTime = document.querySelector(".milTime");
const $startBtn = document.querySelector(".startBtn");
const $stopBtn = document.querySelector(".stopBtn");
const $resetBtn = document.querySelector(".resetBtn");
const $clearBtn = document.querySelector(".clearBtn");
const $recordList = document.querySelector(".recordList");
const $allCheck = document.querySelector(".allCheckBox");

let timer;
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
  clearInterval(timer);
  timer = setInterval(increTime, 10);
});

$stopBtn.addEventListener("click", function () {
  clearInterval(timer);

  let checkBox = document.createElement("input");
  checkBox.setAttribute("type", "checkbox");
  checkBox.setAttribute("class", "checkbox");
  let timeRecord = document.createElement("li");
  timeRecord.innerHTML = $secTime.innerHTML + $milTime.innerHTML;

  $recordList.appendChild(checkBox);
  $recordList.appendChild(timeRecord);
});

$resetBtn.addEventListener("click", function () {
  clearInterval(timer);
  sec = 0;
  milSec = 0;
  $secTime.innerHTML = "00:";
  $milTime.innerHTML = "00";
});

function selectAll(selectAll) {
  const checkboxes = document.querySelectorAll('input[type="checkbox"]');

  checkboxes.forEach((checkbox) => {
    checkbox.checked = selectAll.checked;
  });
}

$allCheck.addEventListener("click", function () {
  selectAll(this);
});

// clearList = function () {
//   const clear = document.querySelectorAll('input[type="checkbox"]');
//   if ((clear.checked = true)) {
//     clear.parentElement.parentElement.remove();
//   }
// };

// $clearBtn.addEventListener("click", function () {
//   clearList();
// });
